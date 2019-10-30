from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import json
import os
import platform
import time
import requests
import shutil
from flask_script import bot_train
from flask_script import rep_body
from flask_script import generate_action_script
from flask_script import action_name_generate
from flask_script import server_process
from flask_script import random_pro_generate
from flask_script import random_reply_generate

'''
接口需要的函数及参数
'''

# botId
botId = 1

# apiKey
apiKey = "vhfyUB7spMz5at3olyhE"

# 测试服务器
test_server_ip = "http://127.0.0.1:5000/parse"
test_qa_core_ip = "http://127.0.0.1:5001/webhooks/rest/webhook"
test_task_core_ip = "http://127.0.0.1:5002/webhooks/rest/webhook"

# 服务器地址
server_ip_arr = ["http://192.168.50.112", "http://192.168.50.113"]
server_ip_req = ""  # 当前请求的服务器ip
R1 = []  # 记录74正在服务的人数
R2 = []  # 记录75正在服务的人数
port = ["8100", "8101", "5000", "5001", "5002"]
# 8100:为flask服务器暴露的访问端口号
# 8101：rasa服务器端口

# 训练是否完成标识
# 取值：y为正在训练，n为未训练
flag_server1_train = "n"
flag_server2_train = "n"
# 是否开启计时器
flag_timer = False

# nlu的parse的url
nlu_service_url1 = server_ip_arr[0] + ":" + port[2] + '/parse'
nlu_service_url2 = server_ip_arr[1] + ":" + port[2] + '/parse'
# url1为qa的core服务的url,url2为task的core的url
qa_service_url = server_ip_arr[0] + ":" + port[3] + '/webhooks/rest/webhook'
task_service_url = server_ip_arr[0] + ":" + port[4] + '/webhooks/rest/webhook'

# 后备动作次数记录
unexpect_count = 0

# 根据系统的不同，确定使用的斜杠
if platform.system() == "Windows":
    slash = "\\"
elif platform.system() == "Linux":
    slash = '/'

# __name__代表当前的python文件。把当前的python文件当做一个服务启动
app = Flask(__name__)
CORS(app)

# 允许接收的文件后缀
ALLOWED_EXTENSIONS = {'md', 'yml', 'json'}


# 用于判断文件后缀
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


# 处理培训数据
def file_process(fileList):
    # 获取当前文件所在的目录的上级目录
    basePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    counter = 0
    try:
        while counter <= 2:
            f = fileList["file" + "[" + str(counter) + "]"]
            # 限定post方法，文件列表不为空且为一问一答类型
            if allowed_file(f.filename):
                # 拼凑文件存储路径
                filePath = basePath + slash + "training" + slash + f.filename
                # 打印路径
                print(filePath)
                # 将文件保存到相应路径
                f.save(filePath)
            counter += 1
    except:
        return rep_body.rep_common(201, {})
    # 返回项目根目录
    return basePath + slash


# 请求拦截器
@app.before_request
def change_request_to():
    print("请求地址：" + str(request.path))
    print("请求方法：" + str(request.method))
    print("---请求headers--start--")
    print(str(request.headers).rstrip())
    print("---请求headers--end----")
    print("GET参数：" + str(request.args))
    print("POST参数：" + str(request.data))
    print("POST参数：" + str(request.form))
    print("POST参数：" + str(request.files))


'''
中间件接口
'''


# 1.文字识别接口
@app.route('/nlp_text_re', methods=['POST'])
def nlp_text_task():
    if request.method == 'POST':
        try:
            # 变量声明
            local_useType = "0"
            botType = 0
            core_service_url = ''
            global unexpect_count
            if request.form:
                print("form对象")
                params = request.form.to_dict()
                print(params)
                visitorId = params['visitorId']
                botId = int(params['botId'])
                useType = params['useType']
                local_useType = useType
            else:
                print("json对象")
                params = request.json
                visitorId = params['visitorId']
                botId = params['botId']
                useType = params['useType']
                local_useType = useType

            print(params)
            inputText = params['inputText']
            print(inputText)
            api_key = params['apiKey']
            # 验证参数
            if api_key == apiKey and botId == 1:
                # 获取最新的qa和task模型名称
                basePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
                qa_path = basePath + slash + "now_models" + slash + "nlu" + slash + "qa"
                qa_model_num = 0
                for index, filename in enumerate(os.listdir(qa_path)):
                    if index != 0:
                        temp_filename_num = int(filename.replace("qa_", ""))
                        if temp_filename_num >= qa_model_num:
                            qa_model_num = temp_filename_num
                    else:
                        qa_model_num = int(filename.replace("qa_", ""))

                task_path = basePath + slash + "now_models" + slash + "nlu" + slash + "task"
                task_model_num = 0
                for index, filename in enumerate(os.listdir(task_path)):
                    if index != 0:
                        temp_filename_num = int(filename.replace("task_", ""))
                        if temp_filename_num >= task_model_num:
                            task_model_num = temp_filename_num
                    else:
                        task_model_num = int(filename.replace("task_", ""))

                # 注释：加入qa后取消注释
                qa_model_name = "qa_" + str(qa_model_num)
                nlu_service_params1 = {"q": inputText, "project": "qa", "model": qa_model_name}
                # nlu_service_response1 = requests.post(nlu_service_url1, data=json.dumps(nlu_service_params1)).json()
                nlu_service_response1 = requests.post(test_server_ip, data=json.dumps(nlu_service_params1)).json()
                task_model_name = "task_" + str(task_model_num)
                nlu_service_params2 = {"q": inputText, "project": "task", "model": task_model_name}
                # nlu_service_response2 = requests.post(nlu_service_url1, data=json.dumps(nlu_service_params2)).json()
                nlu_service_response2 = requests.post(test_server_ip, data=json.dumps(nlu_service_params2)).json()

                print('nlu_service_response1: %s' % nlu_service_response1)
                print('nlu_service_response2: %s' % nlu_service_response2)

                # 一问一答型和任务型机器人的置信度
                bot_confidence1 = nlu_service_response1["intent"]["confidence"]
                bot_confidence2 = nlu_service_response2["intent"]["confidence"]

                print("qa_intent %s" % nlu_service_response1["intent"])
                print('task_intent %s' % nlu_service_response2["intent"])
                if (bot_confidence1 > bot_confidence2 and
                    len(nlu_service_response1["entities"]) == 0 and
                    nlu_service_response2["intent"]['name'] == "task_askfor_again" and
                    local_useType == "2") or \
                        (bot_confidence1 < bot_confidence2 and
                         nlu_service_response2["intent"]['name'] == "task_askfor_again" and
                         local_useType == "2"):
                    askfor_data = {
                        "botId": botId,
                        "botType": 2,
                        "replyText": [],
                        "confidence": 0,
                        "notHeard": "T",
                        "unexpectCount": unexpect_count
                    }
                    return rep_body.rep_common(200, askfor_data)

                # 取一问一答的置信度
                # qa机器人置信度>task机器人置信度，且qa机器人的实体数量不为0
                elif bot_confidence1 > bot_confidence2 and \
                        len(nlu_service_response1["entities"]) != 0:
                    # core_service_url = qa_service_url
                    core_service_url = test_qa_core_ip
                    bot_confidence = bot_confidence1
                    botType = 1

                # 取任务型机器人的置信度
                # 1.qa机器人置信度>task机器人置信度，且qa机器人的实体数量为0，意图不为task_askfor_again
                # 2.qa机器人置信度<=task机器人置信度，且意图不为task_askfor_again
                elif (bot_confidence1 > bot_confidence2 and
                      len(nlu_service_response1["entities"]) == 0 and
                      nlu_service_response2["intent"]['name'] != "task_askfor_again") or \
                        (bot_confidence1 <= bot_confidence2 and
                         nlu_service_response2["intent"]['name'] != "task_askfor_again"):
                    # core_service_url = task_service_url
                    core_service_url = test_task_core_ip
                    bot_confidence = bot_confidence2
                    botType = 2

                # 如果测试窗出现识别出用户未听清的情况,按未识别处理
                elif (bot_confidence1 > bot_confidence2 and
                      len(nlu_service_response1["entities"]) == 0 and
                      nlu_service_response2["intent"]['name'] == "task_askfor_again" and
                      local_useType == "1") or \
                        (bot_confidence1 < bot_confidence2 and
                         nlu_service_response2["intent"]['name'] == "task_askfor_again" and
                         local_useType == "1"):
                    unexpect_count += 1
                    test_list = []
                    test_list.append(random_reply_generate.unrecognized_reply())
                    askfor_data = {
                        "botId": botId,
                        "botType": botType,
                        "replyText": test_list,
                        "confidence": random_pro_generate.random_generate(),
                        "notHeard": "N",
                        "unexpectCount": unexpect_count
                    }
                    if unexpect_count == 2:
                        unexpect_count = 0
                    return rep_body.rep_common(200, askfor_data)

                # 2.把语句发送给合适的nlu对应的core服务
                core_service_params = {"sender": visitorId, "message": inputText}
                core_service_headers = {'content-type': 'application/json'}
                core_service_response = requests.post(core_service_url, data=json.dumps(core_service_params),
                                                      headers=core_service_headers).json()
                print(core_service_response)

                # 3.触发后备动作的记录
                # 遍历core_service_response列表，拼接字符串
                linklist = []
                if len(core_service_response) == 0:
                    unexpect_count += 1
                    # 返回体
                    dictData = {
                        "botId": botId,
                        "botType": botType,
                        "replyText": random_reply_generate.unrecognized_reply(),
                        "confidence": random_pro_generate.random_generate(),
                        "notHeard": "N",
                        "unexpectCount": unexpect_count
                    }
                    if unexpect_count == 2:
                        unexpect_count = 0
                    return rep_body.rep_common(200, dictData)

                for j in core_service_response:
                    linklist.append(j["text"])

                replyText = linklist
                print(replyText)
                print(local_useType)
                # 测试窗
                if local_useType == "1":
                    if replyText[0] == '我还比较小' or replyText[0] == '':
                        unexpect_count += 1
                        bot_confidence = random_pro_generate.random_generate()
                        # 返回体
                        dictData = {
                            "botId": botId,
                            "botType": botType,
                            "replyText": [],
                            "confidence": bot_confidence,
                            "notHeard": "N",
                            "unexpectCount": unexpect_count
                        }
                        if unexpect_count == 2:
                            unexpect_count = 0
                        return rep_body.rep_common(200, dictData)
                    else:
                        # 返回体
                        dictData = {
                            "botId": botId,
                            "botType": botType,
                            "replyText": replyText,
                            "confidence": bot_confidence,
                            "notHeard": "N",
                            "unexpectCount": unexpect_count
                        }
                        return rep_body.rep_common(200, dictData)
                # ccone
                elif local_useType == "2":
                    if replyText[0] == '我还比较小' or replyText[0] == '':
                        unexpect_count += 1
                        replyText = []
                        replyText.append(random_reply_generate.unrecognized_reply())
                        replyText.append(random_reply_generate.morehelp_reply())
                        bot_confidence = random_pro_generate.random_generate()
                        # 返回体
                        dictData = {
                            "botId": botId,
                            "botType": botType,
                            "replyText": replyText,
                            "confidence": bot_confidence,
                            "notHeard": "F",
                            "unexpectCount": unexpect_count
                        }

                        if unexpect_count == 2:
                            unexpect_count = 0
                        return rep_body.rep_common(200, dictData)
                    else:
                        # 返回体
                        dictData = {
                            "botId": botId,
                            "botType": botType,
                            "replyText": replyText,
                            "confidence": bot_confidence,
                            "notHeard": "F",
                            "unexpectCount": unexpect_count
                        }
                        return rep_body.rep_common(200, dictData)
        except Exception as e:
            print(e)
        return rep_body.rep_common(201, {})


#  2.一问一答语料发布
# 删除新的模型，在旧的模型目录训练模型，将训练模型复制到新的模型目录，然后将新模型加载到内存中
@app.route('/nlp_qa_ed', methods=['POST'])
def nlp_qa_ed():
    if request.method == 'POST' and request.files and request.form["d"]:
        global server_ip_req
        global flag_server1_train
        global flag_server2_train
        global flag_timer
        global R1
        global R2
        if flag_timer:
            return rep_body.rep_common(200, {"status": "正在训练中"})
        else:
            if server_ip_req == server_ip_arr[1]:
                flag_server2_train = "y"
                rep = server_process.server_jump(request, request.method, server_ip_req, port[0])
                flag_server2_train = "n"
                rep = jsonify(rep)
                flag_timer = True
                time.sleep(3600)
                R1.clear()
                flag_timer = False
                return rep
            elif server_ip_req == server_ip_arr[0]:
                # 训练标志设置为y
                flag_server1_train = "y"
                fqList = request.files
                d = json.loads(request.form["d"])
                id = d["botId"]
                # 判断botId值
                if not id == botId:
                    return rep_body.rep_common(201, {})
                # 处理培训数据
                path_prefix = file_process(fqList)
                # 生成时间戳
                time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())
                # nlu和core的目录路径
                nlu_path = path_prefix + "now_models" + slash + "nlu"
                core_path = path_prefix + "now_models" + slash + "core"
                # 使用训练服务器进行训练
                # 1.关闭rasa服务
                req_host = server_ip_req + ":" + port[1]
                req_url1 = req_host + "/rasa_server_stop"
                rasa_rep = requests.get(req_url1).json()
                if rasa_rep["code"] == 200:
                    # 删除运行模型目录下的nlu模型和core模型
                    if os.path.exists(nlu_path) and os.path.exists(core_path):
                        shutil.rmtree(nlu_path)
                        shutil.rmtree(core_path)
                        # 新建运行模型目录
                        os.mkdir(nlu_path)
                        os.mkdir(nlu_path + slash + "qa")
                        os.mkdir(nlu_path + slash + "task")
                        os.mkdir(core_path)
                    # 2.训练nlu和core模型
                    qa_model_path = bot_train.train_qa_nlu(path_prefix, slash, time_str)
                    core_model_path = bot_train.train_core(path_prefix, slash, time_str)
                    # 经过替换
                    now_qa_path = qa_model_path.replace('old', 'now')
                    now_core_path = core_model_path.replace('old', 'now')
                    # 复制训练模型(包括nlu、core)到运行模型目录
                    shutil.copytree(qa_model_path, now_qa_path)
                    shutil.copytree(core_model_path, now_core_path)
                    # 3.开启rasa相关服务
                    # nlu服务
                    req_url2 = req_host + "/nlu_server_start"
                    rasa_nlu_rep = requests.get(req_url2).json()
                    # qa服务
                    rasa_qa_data = {"timestr": time_str}
                    h = {"Content-Type": "application/json"}
                    req_url3 = req_host + "/qa_core_server_start"
                    rasa_qa_rep = requests.post(req_url3, data=json.dumps(rasa_qa_data), headers=h).json()
                    # task服务
                    rasa_qa_data = {"timestr": time_str}
                    h = {"Content-Type": "application/json"}
                    req_url4 = req_host + "/task_core_server_start"
                    rasa_task_rep = requests.post(req_url4, data=json.dumps(rasa_qa_data), headers=h).json()
                    # 动作服务
                    req_url5 = req_host + "/rasa_server_sdk"
                    rasa_action_rep = requests.get(req_url5).json()
                    if rasa_nlu_rep["code"] == 200 and rasa_qa_rep["code"] == 200 and rasa_task_rep["code"] == 200 and \
                            rasa_action_rep["code"] == 200:
                        # 新模型加载到内存
                        nlu_service_params1 = {"q": "", "project": "qa", "model": "qa_" + time_str}
                        requests.post(nlu_service_url1, data=json.dumps(nlu_service_params1)).json()
                        nlu_service_params2 = {"q": "", "project": "task", "model": "task_" + time_str}
                        requests.post(nlu_service_url1, data=json.dumps(nlu_service_params2)).json()
                        flag_server1_train = "n"
                        flag_timer = True
                        time.sleep(3600)
                        R2.clear()
                        flag_timer = False
                        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 3.自定义Action名生成
@app.route('/nlp_generate_actionname', methods=['POST'])
def nlp_generate_actionname():
    if request.method == 'POST':
        global server_ip_req
        global flag_server1_train
        global flag_server2_train
        global flag_timer
        global R1
        global R2
        if server_ip_req == server_ip_arr[1]:
            rep = server_process.server_jump(request, request.method, server_ip_req, port[0])
            rep = jsonify(rep)
            return rep
        elif server_ip_req == server_ip_arr[0]:
            req_d = request.json
            bId = req_d["botId"]
            action_flag = req_d["action_flag"]
            if not bId == botId:
                return rep_body.rep_common(201, {})
            if action_flag == "n":
                return rep_body.rep_common(200, {})
            elif action_flag == "y":
                # domain文件的文件路径
                basePath = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
                domainPath = basePath + slash + "training" + slash + "domain.yml"
                # 生成自定义动作名
                dic_actionname = action_name_generate.action_name_generate(domainPath)

            return rep_body.rep_common(200, dic_actionname)

    return rep_body.rep_common(201, {})


# 4.任务流语料发布
# 接收文件
@app.route('/nlp_task_ed', methods=['POST'])
def nlp_task_ed():
    if request.method == 'POST' and request.files and request.form["d"]:
        global server_ip_req
        global flag_server1_train
        global flag_server2_train
        global flag_timer
        global R1
        global R2
        if flag_timer:
            return rep_body.rep_common(200, {"status": "正在训练中"})
        else:
            if server_ip_req == server_ip_arr[1]:
                flag_server2_train = "y"
                rep = server_process.server_jump(request, request.method, server_ip_req, port[0])
                flag_server2_train = "n"
                rep = jsonify(rep)
                flag_timer = True
                time.sleep(3600)
                R1.clear()
                flag_timer = False
                return rep
            elif server_ip_req == server_ip_arr[0]:
                flag_server1_train = "y"
                fqList = request.files
                d = json.loads(request.form["d"])
                bot_id = d["botId"]
                # 判断botId值
                if not bot_id == botId:
                    return rep_body.rep_common(201, {})
                # 处理培训数据
                path_prefix = file_process(fqList)
                # 生成时间戳
                time_str = time.strftime("%Y%m%d%H%M%S", time.localtime())
                # nlu和core的目录路径
                nlu_path = path_prefix + "now_models" + slash + "nlu"
                core_path = path_prefix + "now_models" + slash + "core"
                # 使用训练服务器进行训练
                # 1.关闭rasa服务
                req_host = server_ip_req + ":" + port[1]
                req_url1 = req_host + "/rasa_server_stop"
                rasa_rep = requests.get(req_url1).json()
                if rasa_rep["code"] == 200:
                    # 删除运行模型目录下的nlu模型和core模型
                    if os.path.exists(nlu_path) and os.path.exists(core_path):
                        shutil.rmtree(nlu_path)
                        shutil.rmtree(core_path)
                        # 新建运行模型目录
                        os.mkdir(nlu_path)
                        os.mkdir(nlu_path + slash + "qa")
                        os.mkdir(nlu_path + slash + "task")
                        os.mkdir(core_path)
                # 训练nlu和core模型
                task_model_path = bot_train.train_task_nlu(path_prefix, slash, time_str)
                core_model_path = bot_train.train_core(path_prefix, slash, time_str)
                # 经过替换
                now_task_path = task_model_path.replace('old', 'now')
                now_core_path = core_model_path.replace('old', 'now')
                # 复制训练模型(包括nlu、core)到运行模型目录
                shutil.copytree(task_model_path, now_task_path)
                shutil.copytree(core_model_path, now_core_path)

                # 如果有自定义行为
                if any(d["action"]):
                    # 取得自定义action的dict
                    dic_action = d["action"]
                    # 以下字段均为自定义action信息
                    method = dic_action["method"]  # 请求方式
                    action_name = dic_action["action_name"]  # 动作名字
                    action_url = dic_action["url"]  # 请求url
                    action_data = dic_action["data"]  # 请求数据
                    action_rule = dic_action["rule"]  # 返回模板

                    # 后端给定参数s
                    headers = {'Content-Type': 'application/json'}  # 头部
                    mid_url = "http://" + ""  # 中间件url
                    path = "../action.py"  # 写入的action.py文件的路径

                    generate_action_script.new_action(method, action_name, action_url, action_data,
                                                      action_rule, headers, mid_url, path)
                # 3.开启rasa相关服务
                # nlu服务
                req_url2 = req_host + "/nlu_server_start"
                rasa_nlu_rep = requests.get(req_url2).json()
                # qa服务
                rasa_qa_data = {"timestr": time_str}
                h = {"Content-Type": "application/json"}
                req_url3 = req_host + "/qa_core_server_start"
                rasa_qa_rep = requests.post(req_url3, data=json.dumps(rasa_qa_data), headers=h).json()
                # task服务
                rasa_qa_data = {"timestr": time_str}
                h = {"Content-Type": "application/json"}
                req_url4 = req_host + "/task_core_server_start"
                rasa_task_rep = requests.post(req_url4, data=json.dumps(rasa_qa_data), headers=h).json()
                # 动作服务
                req_url5 = req_host + "/rasa_server_sdk"
                rasa_action_rep = requests.get(req_url5).json()
                if rasa_nlu_rep["code"] == 200 and rasa_qa_rep["code"] == 200 and rasa_task_rep["code"] == 200 and \
                        rasa_action_rep["code"] == 200:
                    # 新模型加载到内存
                    nlu_service_params1 = {"q": "", "project": "qa", "model": "qa_" + time_str}
                    requests.post(nlu_service_url1, data=json.dumps(nlu_service_params1)).json()
                    nlu_service_params2 = {"q": "", "project": "task", "model": "task_" + time_str}
                    requests.post(nlu_service_url1, data=json.dumps(nlu_service_params2)).json()
                    flag_server1_train = "n"
                    flag_timer = True
                    time.sleep(3600)
                    R2.clear()
                    flag_timer = False
                    return rep_body.rep_common(200, {})

    return rep_body.rep_common(201, {})


@app.route("/t")
def hello():
    # print("niaho1")
    # return ""
    return "<h1 style='color:blue'>Hello There!</h1>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

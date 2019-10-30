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

# 后备动作次数记录
unexpect_count = 0

# 根据系统的不同，确定使用的斜杠
slash = "/"
if platform.system() == "Windows":
    slash = "\\"
elif platform.system() == "Linux":
    slash = "/"

# __name__代表当前的python文件。把当前的python文件当做一个服务启动
app = Flask(__name__)
CORS(app)

server_ip = "http://127.0.0.1"
# server_ip = "http://192.168.50.112"

port = ["8100", "8101", "5000", "5001", "5002", "8999"]

# 接口字符串
port_text_reply1 = "/nlp_text_re"
port_text_reply2 = "/nlp_text_task"
port_text_reply3 = "/nlp_text_anyq"

nlu_request_url = server_ip + ":" + port[2] + "/parse"
task_request_url = server_ip + ":" + port[4] + "/webhooks/rest/webhook"
# nlu_request_url = "http://192.168.230.45" + ":" + port[2] + "/parse"
# task_request_url = "http://192.168.230.45" + ":" + port[4] + "/webhooks/rest/webhook"

qa_request_url = server_ip + ":" + port[3] + "/webhooks/rest/webhook"
anyq_request_url = server_ip + ":" + port[5] + "/anyq"
# qa_request_url = "http://192.168.50.74" + ":" + port[3] + "/webhooks/rest/webhook"
# anyq_request_url = "http://192.168.50.74" + ":" + port[5] + "/anyq"

# apiKey
apiKey = "vhfyUB7spMz5at3olyhE"


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


# 1.文字识别接口(新)
@app.route(port_text_reply1, methods=['POST']) # port_text_reply1 = "/nlp_text_re"
def nlp_text_re():
    if request.method == 'POST':
        try:
            # 变量声明
            bot_type = 0
            core_service_url = ''
            global unexpect_count
            if request.form:
                # print("form对象")
                params = request.form.to_dict()
                # print("form对象的params：" % params)
                visitor_id = params['visitorId']
                bot_id = int(params['botId'])
                use_type = params['useType']
            else:
                # print("json对象")
                params = request.json
                # print("json对象的params：" % params)
                visitor_id = params['visitorId']
                bot_id = params['botId']
                use_type = params['useType']
            if type(visitor_id) == str:
                visitor_id = int(visitor_id.replace("voice", ""))
            # print("解析出的对象:" % params)
            input_text = params['inputText']
            # print("input_text" + input_text)
            api_key = params['apiKey']
            # 验证参数
            if api_key == apiKey and bot_id == 1:
                # 获取最新的qa和task模型名称
                base_path = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
                task_path = base_path + slash + "now_models" + slash + "nlu" + slash + "task"
                task_model_num = 0
                for index, filename in enumerate(os.listdir(task_path)):
                    if index != 0:
                        temp_filename_num = int(filename.replace("task_", ""))
                        if temp_filename_num >= task_model_num:
                            task_model_num = temp_filename_num
                    else:
                        task_model_num = int(filename.replace("task_", ""))

                # AnyQ一问一答返回结果
                anyq_url = anyq_request_url + "?question=" + input_text
                # print("anyq_url:" + anyq_url)
                anyq_response = requests.get(anyq_url)
                if anyq_response.content:
                    anyq_service_response = anyq_response.json()
                    # global anyq_service_response # zhang 声明  anyq_service_response为全局变量 2019/10/23  10：00 添加
                    # print("anyq_service_response:" % anyq_service_response)

                task_model_name = "task_" + str(task_model_num)
                nlu_service_params2 = {"q": input_text, "project": "task", "model": task_model_name}
                # print("nlu_request_url:" + nlu_request_url)
                # print("nlu_service_params2:" % nlu_service_params2)
                nlu_service_response2 = requests.post(nlu_request_url, data=json.dumps(nlu_service_params2)).json()

                # print('nlu_service_response2: %s' % nlu_service_response2)

                # 一问一答型机器人置信度
                if anyq_response.content:

                    if len(anyq_service_response) != 0:
                        bot_confidence1 = anyq_service_response[0]["confidence"]
                    else:
                        bot_confidence1 = 0
                else:
                    bot_confidence1 = 0
                # 任务型机器人置信度
                if any(nlu_service_response2):
                    bot_confidence2 = nlu_service_response2["intent"]["confidence"]
                else:
                    return rep_body.rep_common(201, {})

                # # print("qa_intent %s" % nlu_service_response1["intent"])
                # print('task_intent %s' % nlu_service_response2["intent"])

                # 一问一答型机器人回复
                # round 返回浮点数的后几位  ps: round(3.1415,2) ---> 3.14
                if (bot_confidence1 > bot_confidence2) or (
                        round(bot_confidence1, 1) == round(bot_confidence2, 1)) and anyq_response.content:
                    anyq_answer = anyq_service_response[0]["answer"]
                    # print("ananyq_answer:" % anyq_answer)
                    bot_type = 1
                    askfor_data = {
                        "botId": bot_id,
                        "botType": bot_type,
                        "replyText": [anyq_answer],
                        "confidence": bot_confidence1,
                        "notHeard": "N",
                        "unexpectCount": unexpect_count
                    }
                    return rep_body.rep_common(200, askfor_data)

                # 任务型机器人回复
                else:
                    bot_type = 2
                    # 测试窗
                    if use_type == "1":
                        not_heard = "N"
                        # 1.排除测试窗的外呼意图、转人工意图和用户听不清楚的影响
                        if (nlu_service_response2['intent']['name'] == 'task_kuandai_huifang'
                                or nlu_service_response2['intent']['name'] == 'task_to_people'
                                or nlu_service_response2['intent']['name'] == 'task_askfor_again'):
                            unexpect_count += 1
                            reply_text = []
                            reply_text.append(random_reply_generate.unrecognized_reply())
                            reply_text.append(random_reply_generate.morehelp_reply())
                            bot_confidence = random_pro_generate.random_generate()
                            # 返回体
                            dict_data = {
                                "botId": bot_id,
                                "botType": use_type,
                                "replyText": reply_text,
                                "confidence": bot_confidence,
                                "notHeard": not_heard,
                                "unexpectCount": unexpect_count
                            }
                            if unexpect_count == 2:
                                unexpect_count = 0
                            return rep_body.rep_common(200, dict_data)
                        # 2.测试窗正常处理
                        else:
                            core_service_url = task_request_url
                            bot_confidence = bot_confidence2
                            # 请求task的core服务
                            core_service_params = {"sender": visitor_id, "message": input_text}
                            # print("测试窗的core_service_params：" % core_service_params)
                            core_service_headers = {'content-type': 'application/json'}
                            core_service_response = requests.post(core_service_url,
                                                                  data=json.dumps(core_service_params),
                                                                  headers=core_service_headers).json()
                            # print("core_service_response" % core_service_response)
                            # 机器人响应的处理
                            linklist = []
                            if len(core_service_response) == 0:
                                unexpect_count += 1
                                # 返回体
                                dict_data = {
                                    "botId": bot_id,
                                    "botType": bot_type,
                                    "replyText": random_reply_generate.unrecognized_reply(),
                                    "confidence": random_pro_generate.random_generate(),
                                    "notHeard": not_heard,
                                    "unexpectCount": unexpect_count
                                }
                                if unexpect_count == 2:
                                    unexpect_count = 0
                                return rep_body.rep_common(200, dict_data)

                            for j in core_service_response:
                                linklist.append(j["text"])

                            reply_text = linklist
                            # print("测试窗的reply_text:" % reply_text)
                            if reply_text[0] == '我还比较小' or reply_text[0] == '':
                                unexpect_count += 1
                                reply_text = []
                                reply_text.append(random_reply_generate.unrecognized_reply())
                                reply_text.append(random_reply_generate.morehelp_reply())
                                bot_confidence = random_pro_generate.random_generate()
                                # 返回体
                                dict_data = {
                                    "botId": bot_id,
                                    "botType": bot_type,
                                    "replyText": reply_text,
                                    "confidence": bot_confidence,
                                    "notHeard": not_heard,
                                    "unexpectCount": unexpect_count
                                }
                                if unexpect_count == 2:
                                    unexpect_count = 0
                                return rep_body.rep_common(200, dict_data)
                            else:
                                # 返回体
                                dict_data = {
                                    "botId": bot_id,
                                    "botType": bot_type,
                                    "replyText": reply_text,
                                    "confidence": bot_confidence,
                                    "notHeard": not_heard,
                                    "unexpectCount": unexpect_count
                                }
                                return rep_body.rep_common(200, dict_data)
                    # 语音
                    elif use_type == "2":
                        not_heard = "F"
                        # 1.处理转人工意图
                        if nlu_service_response2['intent']['name'] == 'task_to_people':
                            reply_text = []
                            not_heard = "P"
                            reply_text.append(random_reply_generate.morehelp_reply())
                            bot_confidence = nlu_service_response2['intent']['confidence']
                            # 返回体
                            dict_data = {
                                "botId": bot_id,
                                "botType": use_type,
                                "replyText": reply_text,
                                "confidence": bot_confidence,
                                "notHeard": not_heard,
                                "unexpectCount": unexpect_count
                            }
                            return rep_body.rep_common(200, dict_data)


                        # 2.语音出现用户未听清的情况
                        elif nlu_service_response2["intent"]['name'] == "task_askfor_again":
                            not_heard = "T"
                            # 语音出现用户未听清的情况
                            askfor_data = {
                                "botId": bot_id,
                                "botType": bot_type,
                                "replyText": [],
                                "confidence": 0,
                                "notHeard": not_heard,
                                "unexpectCount": unexpect_count
                            }
                            return rep_body.rep_common(200, askfor_data)

                        # 3.用户听清机器人的回复
                        elif nlu_service_response2["intent"]['name'] != "task_askfor_again":
                            # 处理用户的再见意图
                            if nlu_service_response2['intent']['name'] == 'goodbye':
                                not_heard = "G"
                            core_service_url = task_request_url
                            bot_confidence = bot_confidence2
                            # 请求task的core服务
                            core_service_params = {"sender": visitor_id, "message": input_text}
                            # print("语音的core_service_params:" % core_service_params)
                            core_service_headers = {'content-type': 'application/json'}
                            core_service_response = requests.post(core_service_url,
                                                                  data=json.dumps(core_service_params),
                                                                  headers=core_service_headers).json()
                            # print("语音的core_service_response:" % core_service_response)

                            # 机器人响应的处理
                            linklist = []
                            if len(core_service_response) == 0:
                                unexpect_count += 1
                                # 返回体
                                dict_data = {
                                    "botId": bot_id,
                                    "botType": bot_type,
                                    "replyText": random_reply_generate.unrecognized_reply(),
                                    "confidence": random_pro_generate.random_generate(),
                                    "notHeard": not_heard,
                                    "unexpectCount": unexpect_count
                                }
                                if unexpect_count == 2:
                                    unexpect_count = 0
                                return rep_body.rep_common(200, dict_data)

                            for j in core_service_response:
                                linklist.append(j["text"])

                            reply_text = linklist
                            # print("语音的reply_text：" % reply_text)
                            if reply_text[0] == '我还比较小' or reply_text[0] == '':
                                unexpect_count += 1
                                reply_text = []
                                reply_text.append(random_reply_generate.unrecognized_reply())
                                reply_text.append(random_reply_generate.morehelp_reply())
                                bot_confidence = random_pro_generate.random_generate()
                                # 返回体
                                dict_data = {
                                    "botId": bot_id,
                                    "botType": bot_type,
                                    "replyText": reply_text,
                                    "confidence": bot_confidence,
                                    "notHeard": not_heard,
                                    "unexpectCount": unexpect_count
                                }

                                if unexpect_count == 2:
                                    unexpect_count = 0
                                return rep_body.rep_common(200, dict_data)
                            else:
                                # 返回体
                                dict_data = {
                                    "botId": bot_id,
                                    "botType": bot_type,
                                    "replyText": reply_text,
                                    "confidence": bot_confidence,
                                    "notHeard": not_heard,
                                    "unexpectCount": unexpect_count
                                }
                                return rep_body.rep_common(200, dict_data)
        except Exception as e:
            # print(type(e))
            # print(e)
            # print('错误')
            return rep_body.rep_common(201, {"err_msg": str(e)})

#anyq接口
@app.route(port_text_reply3,methods=["POST"]) # port_text_reply3 = "/nlp_text_anyq"
def nlp_text_anyq():
    if request.method == "POST":
        try:
            if request.form:
                params = request.form.to_dict()
                visitor_id = params["visitorId"]
                bot_id = int(params["botId"])
                user_type = params["userType"]
            else:
                params = request.json
                visitor_id = params["visitorId"]
                bot_id = int(params["botId"])
                user_type = params["userType"]
            if type(visitor_id) == str:
                visitor_id = int(visitor_id.replace("voice", ""))

            input_text = params["inputText"]
            api_key = params["apiKey"]

            if api_key == apiKey and bot_id == 1:
                return "中间件之间测试成功了！"
                # # AnyQ一问一答返回结果
                # anyq_url = anyq_request_url + "?question=" + input_text
                # # print("anyq_url:" + anyq_url)
                # anyq_response = requests.get(anyq_url)
                # if anyq_response.content:
                #     anyq_service_response = anyq_response.json()
                #     # print("anyq_service_response:" % anyq_service_response)
                #
                #     # 一问一答型机器人置信度
                #     if len(anyq_service_response) != 0:
                #         bot_confidence1 = anyq_service_response[0]["confidence"]
                #     else:
                #         bot_confidence1 = 0
                #
                #     # 一问一答型机器人回复
                #     # round 返回浮点数的后几位  ps: round(3.1415,2) ---> 3.14
                #     anyq_answer = anyq_service_response[0]["answer"]
                #     # print("ananyq_answer:" % anyq_answer)
                #     bot_type = 1
                #     askfor_data = {
                #         "botId": bot_id,
                #         "botType": bot_type,
                #         "replyText": [anyq_answer],
                #         "confidence": bot_confidence1,
                #         "notHeard": "N",
                #         "unexpectCount": unexpect_count
                #     }
                #     return rep_body.rep_common(200, askfor_data)
        except Exception as e:
            return  rep_body.rep_common(201, {"err_msg": str(e)})


# 启动nlu服务器
@app.route("/nlu_server_start", methods=['GET'])
def start_nlu_server():
    if request.method == 'GET':
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startNluServer.sh"
        try:
            os.popen(path)
        except Exception as e:
            # print(e)
            return rep_body.rep_common(201, {})
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 启动qa的core服务
# 接收的参数为时间戳
@app.route("/qa_core_server_start", methods=['POST'])
def qa_core_server_start():
    if request.method == 'POST' and 'timestr' in request.json:
        timestr = request.json['timestr']
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startQaCoreServer.sh"
        os.popen(path + " " + timestr)
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 启动task的core服务
# 接收的参数为时间戳
@app.route("/task_core_server_start", methods=['POST'])
def task_core_server_start():
    if request.method == 'POST' and 'timestr' in request.json:
        timestr = request.json['timestr']
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startTaskCoreServer.sh"
        os.popen(path + " " + timestr)
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 开启动作服务器
@app.route("/rasa_server_sdk", methods=['GET'])
def rasa_server_sdk():
    if request.method == 'GET':
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startSdkServer.sh"
        try:
            os.popen(path)
        except Exception as e:
            # print(e)
            return rep_body.rep_common(201, {})
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 关闭rasa服务器
@app.route("/rasa_server_stop", methods=['GET'])
def rasa_server_stop():
    if request.method == 'GET':
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/stopRasaServer.sh"
        try:
            os.popen(path)
        except Exception as e:
            # print(e)
            return rep_body.rep_common(201, {})
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


@app.route("/t")
def hello():
    # # print("niaho1")
    # return ""
    return "<h1 style='color:blue'>Hello There!</h1>"




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8888)

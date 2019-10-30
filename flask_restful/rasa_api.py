import os
from flask import request
from flask import Flask
from flask_cors import CORS
from flask_script import rep_body

rasa_server = Flask(__name__)
CORS(rasa_server)


# 启动nlu服务器
@rasa_server.route("/nlu_server_start", methods=['GET'])
def start_nlu_server():
    if request.method == 'GET':
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startNluServer.sh"
        try:
            os.popen(path)
        except Exception as e:
            print(e)
            return rep_body.rep_common(201, {})
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 启动qa的core服务
# 接收的参数为时间戳
@rasa_server.route("/qa_core_server_start", methods=['POST'])
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
@rasa_server.route("/task_core_server_start", methods=['POST'])
def task_core_server_start():
    if request.method == 'POST' and 'timestr' in request.json:
        timestr = request.json['timestr']
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startTaskCoreServer.sh"
        os.popen(path + " " + timestr)
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})


# 开启动作服务器
@rasa_server.route("/rasa_server_sdk", methods=['GET'])
def rasa_server_sdk():
    if request.method == 'GET':
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/startSdkServer.sh"
        try:
            os.popen(path)
        except Exception as e:
            print(e)
            return rep_body.rep_common(201, {})
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})

# 关闭rasa服务器
@rasa_server.route("/rasa_server_stop", methods=['GET'])
def rasa_server_stop():
    if request.method == 'GET':
        # .sh脚本文件绝对路径
        path = "/rasa/zndhjqr_nlp/rasa_shell/stopRasaServer.sh"
        try:
            os.popen(path)
        except Exception as e:
            print(e)
            return rep_body.rep_common(201, {})
        return rep_body.rep_common(200, {})
    return rep_body.rep_common(201, {})



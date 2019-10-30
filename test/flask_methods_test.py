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
from flask_script import rep_body

app = Flask(__name__)
CORS(app)

# apiKey
apiKey = "vhfyUB7spMz5at3olyhE"


# 1.get请求
@app.route('/axiosT', methods=["GET"])
def axiosT():
    if request.method == 'GET':
        # 返回体
        dictData = {
            "msg": "并发1成功"
        }
        return rep_body.rep_common(200, dictData)

    return rep_body.rep_common(201, {})

# 2.get请求
@app.route('/iT', methods=["GET"])
def iT():
    if request.method == 'GET':
        # 返回体
        dictData = {
            "token": "abc"
        }
        return jsonify(dictData)

    return rep_body.rep_common(201, {})


# 2.post请求
@app.route('/po', methods=["POST"])
def po():
    if request.method == 'POST':
        if request.json["a"] == 1:
            # 返回体
            dictData = {
                "msg": "并发2成功"
            }
            return rep_body.rep_common(200, dictData)

    return rep_body.rep_common(201, {})


# 2.post请求
@app.route('/sd', methods=["POST"])
def sd():
    if request.method == 'POST':
        if request.json["sd"] == 1:
            # 返回体
            dictData = {
                "msg": "post请求成功"
            }
            return rep_body.rep_common(200, dictData)

    return rep_body.rep_common(201, {})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)

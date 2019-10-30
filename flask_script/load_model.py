import requests
import json


# 通过向nlu服务器发送parse请求（用于向指定模型发送语句请求意图识别置信度）的方式将模型上载到nlu模型服务器内存
def load_model():
    # 请求的数据，需指定项目名和模型名
    ml_loaddata = {
        "q": "load",
        "project": "nlu_p1",
        "model": "model1"
    }
    m2_loaddata = {
        "q": "load",
        "project": "nlu_p2",
        "model": "model2"
    }
    # 请求的URL
    load_url = "http://localhost:5000/parse"
    headers = {'content-type': 'application/json'}
    # 发送请求
    requests.post(load_url, data=json.dumps(ml_loaddata), headers=headers)
    requests.post(load_url, data=json.dumps(m2_loaddata), headers=headers)


if __name__ == "__main__":
    load_model()

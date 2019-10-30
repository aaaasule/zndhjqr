import json
import requests


# req:flask中的request请求
# req_method:请求方法
# req_ip：请求ip
# port：请求端口号数组
# R_arr：数组ip
# flag:判断是否训练请求，y为是,n为否
# timestr:表明是否运行rasa模型
def server_jump(req, req_method, req_ip, port, flag=None):
    # 方法url
    req_path = req.path
    # 请求url
    req_url = req_ip + port + req_path
    # 发送的是文件
    if req_method == "POST" and flag == "y":
        print(req.form)
        req_data = req.form.to_dict()
        req_files = req.files.to_dict()
        f1 = req_files["file[0]"]
        f2 = req_files["file[1]"]
        f3 = req_files["file[2]"]
        # 文件相关参数
        req_files_data = {
            "file[0]": (f1.filename, f1.stream, f1.content_type, f1.headers),
            "file[1]": (f2.filename, f2.stream, f2.content_type, f2.headers),
            "file[2]": (f3.filename, f3.stream, f3.content_type, f3.headers),
        }
        return requests.post(req_url, data=req_data, files=req_files_data).json()
    elif req_method == "POST" and flag == None:
        h = {"Content-Type": "application/json"}
        return requests.post(req_url, data=json.dumps(req.json), headers=h).json()

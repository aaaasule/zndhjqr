# encoding=utf-8
'''
新action写入脚本
脚本功能说明：
将用户定义的action写入action.py文件
action的run方法功能为：
访问URL转接中间件，将用户给出的URL、method（“post”或“get”）和访问参数传递给URL转接中间件，接受来自URL转接中间件的返回数据，以其中的code码判定访问成功或失败，若失败，返回提示给用户，若成功，将返回数据按用户给定的输出格式返回。
用户给出的输出规则格式为:
以“{}”包裹语句中需要填入的词汇，“{}”中给出此词汇在URL返回值中对应的key
如下所示：
"今天{city}的天气为{weather}，气温为{tem}"
规定用户提供的URL返回值为字典格式的json数据，用户给的规则中的缺口应被包含在此字典最外层的键中
还需判断用户新建的动作名是否已存在
需判断用户给出的规则中填写的键名是否正确
需要的参数：
"method":"post" or "get"(str类型)     # 用户选定的URL请求方式(必选)
"name":name(str类型)                 # 动作名（后端生成）
"url":URL(str类型)                # 用户定义的动作需访问的URL（必填）
"data":data(dict类型)               # 访问URL时需传输的数据(必填)
"headers":hesders(dict类型)         # 访问URL时所需的请求头(后端给定)
"rule":rule(str类型)           # 用户给出的输出规则(选填)
"mid_url":(str类型)               # 中间件的url(后端给出)
"path":path(str类型)           # 被写入的action.py文件的路径，由后端给出，默认给path="./action.py"
'''


def new_action(method, name, url, data, headers, rule, mid_url, path="./action.py"):
    # 追加模式打开文件
    with open(path, "ab") as act_file:
        # 拼接写入的字符串
        action_str = """\n\n""" + """class """ + name + """(Action):""" \
                     + """\n\t""" + """def name(self):""" + """\n""" \
                     + """\t\t""" + """return '""" + name + """' """ \
                     + """\n\n\t""" + """def run(self, dispatcher, tracker, domain):""" \
                     + """\n\t\t""" + """data = """ + str(data) \
                     + """\n\t\t""" + """method = '""" + method + """'""" \
                     + """\n\t\t""" + """url = '""" + url + """'""" \
                     + """\n\t\t""" + """mid_url = '""" + mid_url + """'""" \
                     + """\n\t\t""" + """headers = """ + str(headers)  \
                     + """\n\t\t""" + """rule = '""" + rule + """'""" \
                     + """\n\t\t""" + """rep = requests.post(mid_url, data=json.dumps(data), headers=headers).json()""" \
                     + """\n\t\t""" + """if str(rep["code"]) == "0":""" \
                     + """\n\t\t\t""" + """if rule != "":""" \
                     + """\n\t\t\t\t""" + """bot_mess = rule.format(**rep)""" \
                     + """\n\t\t\t\t""" + """dispatcher.utter_message(bot_mess)""" \
                     + """\n\t\t\t""" + """else:""" \
                     + """\n\t\t\t\t""" + """dispatcher.utter_message(str(rep))""" \
                     + """\n\t\t""" + """else:""" \
                     + """\n\t\t\t""" + """dispatcher.utter_message("访问ulr失败")""" \
                     + """\n\t\t""" + """return []"""
        action_str = action_str.encode("utf-8")
        act_file.write(action_str)
    act_file.close()
    return path


# 模拟写入action
if __name__ == "__main__":
    method = "post"
    name = "demoaction"
    url = "adsfasfadsfasdf"
    data = {
        "q": "",
        "project": "nlu_p4",
        "model": "model4"
    }
    headers = {
        "q": "",
        "project": "nlu_p4",
        "model": "撒旦法"
    }
    rule = "00000000000000000"
    mid_url = "1111111111111111"
    print(new_action(method, name, url, data, headers, rule, mid_url))

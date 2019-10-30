import yaml
import string
import random


def action_name_generate(domainPath):
    # 读取domain文件中的所有自定义action名字，组成一个action_list
    with open(domainPath, 'r', encoding="utf-8") as f:
        yml_data = f.read()
        yml_dict = yaml.load(yml_data)
    yml_dict["actions"].append("action_listen")
    yml_dict["actions"].append("action_restart")
    yml_dict["actions"].append("action_default_fallback")
    action_list = yml_dict["actions"]  # 组成已经存在的自定义动作列表
    action_name = ""
    # 判断是否为有效的自定义动作名
    # 有效，则直接返回有效的自定义动作名
    # 无效，则继续生成自定义动作名
    while action_name in action_list or action_name == "":
        # 随机生成五位小写字母组成的动作名
        random_list = []
        count = 0
        while count < 5:  # 生成5位随机字符串
            s = string.ascii_lowercase  # 小写字母(a-z)
            r = random.choice(s)
            random_list.append(r)
            count += 1
        action_name = "action_" + "".join(random_list)  # 生成随机自定义动作名
        dic_actionname = {"action_name": action_name}
        return  dic_actionname

from rasa_core_sdk import Action
import json
import requests


class CheckTheWeather(Action):
    def name(self):
        return 'action_check_weather'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_template("utter_wait", tracker)
            city = tracker.get_slot("task_check_city")
            city = city.replace(' ', '')
            code = {"北京": 110000, "天津": 120000, "石家庄": 130100, "武汉": 420100, "太原": 140100}
            if city == "北京":
                code = code["北京"]
            elif city == "天津":
                code = code["天津"]
            elif city == "石家庄":
                code = code["石家庄"]
            elif city == "武汉":
                code = code["武汉"]
            elif city == "太原":
                code = code["太原"]
            else:
                dispatcher.utter_message("无法识别该城市")
                return []

            url = "http://api.ip138.com/weather/?code=" + str(code) + "&type=1&token=9e1b942104799ddc96609c6847dab442"

            rep = requests.get(url).json()
            rep_city = rep["city"]
            if rep_city == "":
                rule = "今天{province}的天气为{data[weather]}，平均气温为{data[temp]}℃,{data[wind]}"
            else:
                rule = "今天{city}的天气为{data[weather]}，平均气温为{data[temp]}℃,{data[wind]}"
            if str(rep["ret"]) == "ok":
                bot_mess = rule.format(**rep)
                dispatcher.utter_message(bot_mess)
            else:
                dispatcher.utter_message("访问ulr失败")

        except:
            dispatcher.utter_message("因某些原因，暂时无法查询，希望您谅解")
        return []


class ActionCheckTel(Action):
    def name(self):
        return 'action_check_tel'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_template("utter_wait", tracker)
            idcard = tracker.get_slot("task_idcard")
            idcard = idcard.replace(' ', '')
            print(idcard)
            if int(idcard) == 110227199601173810:
                dispatcher.utter_template("utter_task_id_2", tracker)
            elif int(idcard) == 110227199601173811:
                dispatcher.utter_template("utter_task_id_12", tracker)
            elif int(idcard) == 110227199601173812:
                dispatcher.utter_template("utter_task_id_9", tracker)
        except:
            dispatcher.utter_message("因某些原因，暂时无法查询，希望您谅解")
        return []


class ActionFillinTel(Action):
    def name(self):
        return 'action_fillin_tel'

    def run(self, dispatcher, tracker, domain):
        try:
            dispatcher.utter_template("utter_wait", tracker)
            fillin_tel = tracker.get_slot("fillin_tel")
            fillin_tel = fillin_tel.replace(' ', '')
            print(fillin_tel)
            if int(fillin_tel) == 15166515951:
                dispatcher.utter_message("请您确认：您的姓名是：张树海，地址是：河北省邯郸市丛台一片区丛台区31区滏河北大街润实月亮湾小区01-1701")
            elif int(fillin_tel) == 15166516666:
                dispatcher.utter_message("请您确认：关羽，北京蓝宝大厦2022")
            elif int(fillin_tel) == 15166517777:
                dispatcher.utter_message("请您确认：张飞，北京蓝宝大厦3033")
            elif int(fillin_tel) == 15166518888:
                dispatcher.utter_message("对不起，没有查询到您的信息，请输入正确的注册电话号码，按井号键确认")
        except:
            dispatcher.utter_message("因某些原因，暂时无法查询，希望您谅解")
        return []





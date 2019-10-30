def predict_parameter(intent, entities, text):
    """
    预测下一步的机器人action
    :param intent: 类型为dict
    :param entities:类型为list
    :param text: 类型为String
    :return:
    """
    predict_list = [
        {
            "event": "action",
            "name": "action_listen"
        },
        {
            "event": "user",
            "parse_data": {
                "entities": [{
                    "start": 0,
                    "end": 2,
                    "value": "北京",
                    "entity": "task_check_city",
                    "confidence": 0.8317215410614769,
                    "extractor": "ner_crf"
                }],
                "intent": {
                    "name": "task_check_weather_2",
                    "confidence": 0.9588183760643005
                },
                "text": "北京"
            },
            "text": "北京"
        }
    ]

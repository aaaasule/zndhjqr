from flask import jsonify



code1 = 200  # 成功状态码
code2 = 201  # 失败状态码


# 公共响应体
# code:状态码
# body_data：响应体中的data数据
def rep_common(code, dict):
    if any(dict) and code == code1:
        return jsonify({
            "code": 200,
            "msg": "success",
            "data": dict
        })
    elif not any(dict) and code == code1:
        return jsonify({
            "code": code,
            "msg": "success",
            "data": {}
        })
    elif not any(dict) and code == code2:
        return jsonify({
            "code": code,
            "msg": "err",
            "data": {}
        })
    elif any(dict) and code == code2:
        return jsonify({
            "code": code,
            "msg": "err",
            "data": dict
        })

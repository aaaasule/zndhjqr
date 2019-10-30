import random


# 生成2e15~6e15的随机数
# 用以处理当识别不出来时，改变意图识别率
def random_generate():
    x = 2e15
    y = 7e15
    random_num = random.randint(x, y)
    random_divisor = 1e16
    random_probability = random_num / random_divisor
    return random_probability
    # print(random_probability)

import random

unrecognized_reply_list = ['对不起，这个问题我还不知道，换一个问题问我吧！',
                           '对不起我不知道该怎么回答您，换一个问题吧！',
                           '这个问题有点难度，我还不知道,换一个问题好吗']

morehelp_reply_list = ["很高兴继续为您服务，还有什么可以帮您？",
                       "为您服务，我感到非常荣幸，请问还有什么能够帮您？",
                       "非常荣幸能为您服务。请问还有什么可以帮助您的吗？"]


def unrecognized_reply():
    """
    生成未识别的随机回复
    :return:随机回复
    """
    i = len(unrecognized_reply_list) - 1
    index = random.randint(0, i)
    return unrecognized_reply_list[index]


def morehelp_reply():
    """
    生成更多帮助的随机回复
    :return: 随机回复
    """
    j = len(morehelp_reply_list) - 1
    index = random.randint(0, j)
    return morehelp_reply_list[index]


if __name__ == "__main__":
    print(unrecognized_reply())
    print(morehelp_reply())

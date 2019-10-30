import jieba
import jieba.posseg as pseg
from typing import Text


def fenci(message: Text):
    # jieba.load_userdict("./dict.txt")
    word_list = jieba.cut(message)
    print("|".join(word_list))
    print(type(word_list))


def biaozhu(message: Text):
    word_list = pseg.cut(message.strip())
    outstr = ''
    for x in word_list:
        outstr += "{}/{},".format(x.word, x.flag)
    print(outstr)


def word_process(text):
    """

    :param text:
    :return:
    """
    result = []
    print(jieba.tokenize(text))
    for (word, start, end) in jieba.tokenize(text):
        pseg_data = [(w, f) for (w, f) in pseg.cut(word)]
        result.append((pseg_data, start, end))

    # result = word_process('我明天去吃饭')
    print(result)
    raw_entities = []
    for (item_posseg, start, end) in result:
        part_of_speech = ["nr", "ns", "nt", "t"]
        for (word_posseg, flag_posseg) in item_posseg:
            print(word_posseg)
            print(flag_posseg)
            if flag_posseg in part_of_speech:
                raw_entities.append({
                    'start': start,
                    'end': end,
                    'value': word_posseg,
                    'entity': flag_posseg
                })
    print(raw_entities)
    # return result


def juzhen():
    # 列表解析
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    list = [row[1] for row in M]
    print(list)  # 输出:[2, 5, 8]


if __name__ == '__main__':
    # jieba.load_userdict('./userdict.txt')
    # biaozhu('我十点去吃饭')
    # print(any({'s':'s'}))
    # print(round(0, 1))
    # for i in range(5):
    #     print(i)
    try:
        if 3/0==4:
            print('s')
    except Exception as e:
        q=str(e)
        print(type(q))
    # pass
    # print(type(3) == )

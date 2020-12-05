import os
import jieba
import codecs
import jieba.posseg as pseg
from get_repeat_names import get_repeat_hash


def analysis_file(text_file, repeat_hash=[]):
    names = {}  # 姓名字典
    relationships = {}  # 关系字典
    lineNames = []  # 每段内人物关系
    with codecs.open(text_file, "r", "utf-8") as f:
        for line in f.readlines():
            poss = pseg.cut(line)  # 分词并返回该词词性
            row = []
            for w in poss:
                if w.flag != "nr" or len(w.word) < 2:
                    continue  # 当分词长度小于2或该词词性不为nr时认为该词不为人名

                # 归一化
                name = w.word
                for k, vs in repeat_hash.items():
                    if name in vs:
                        name = k
                        break

                row.append(name)  # 为当前段的环境增加一个人物
                count = names.get(name, 0)
                names[name] = count + 1  # 该人物出现次数加 1
                if count == 0:
                    relationships[name] = {}
            lineNames.append(row)  # 为新读入的一段添加人物名称列表

    # explore relationships
    for line in lineNames:  # 对于每一段
        for name1 in line:
            for name2 in line:  # 每段中的任意两个人
                if name1 == name2:
                    continue
                re_count = relationships[name1].get(name2, 0)
                relationships[name1][name2] = re_count + 1  # 两人共同出现次数加 1

    return [names, relationships]


def output_files(names, relationships, node_file, edge_file):
    with codecs.open(node_file, "w", "utf-8") as f:
        f.write("Id Label Weight\r\n")
        for name, times in names.items():
            f.write(name + " " + name + " " + str(times) + "\r\n")

    with codecs.open(edge_file, "w", "utf-8") as f:
        f.write("Source Target Weight\r\n")
        for name, edges in relationships.items():
            for v, w in edges.items():
                if w > 3:
                    f.write(name + " " + v + " " + str(w) + "\r\n")


if __name__ == "__main__":
    cwd = os.path.split(os.path.realpath(__file__))[0]
    dict_file = f"{cwd}/dict.txt"
    text_file = f"{cwd}/basic_file.txt"
    node_file = f"{cwd}/node.txt"
    edge_file = f"{cwd}/edge.txt"

    repeat_hash = get_repeat_hash()
    jieba.load_userdict(dict_file)
    print("loaded dict.")
    print("analysis_file")
    names, relationships = analysis_file(text_file, repeat_hash)
    print("output_files")
    output_files(names, relationships, node_file, edge_file)

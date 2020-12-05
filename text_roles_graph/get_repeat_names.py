import os
import codecs


def get_repeat_hash():
    """
    return repeat names
    """
    cwd = os.path.split(os.path.realpath(__file__))[0]
    repeat_dict_file = f"{cwd}/repeat_dict.txt"

    repeat_hash = {}
    with codecs.open(repeat_dict_file, "r", "utf-8") as f:
        for line in f.readlines():
            ws = line.rstrip().split(",")
            repeat_hash[ws[0]] = ws

    return repeat_hash

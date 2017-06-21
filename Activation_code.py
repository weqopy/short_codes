# !/usr/bin/env python
# -*- coding:utf-8 -*-


import string
import random

"""
    'the_string()' 的自定义实现
    # a-z
    word = [chr(i) for i in range(ord('a'), ord('a') + 26)]
    word = ''.join(word)
    # A-Z
    word_up = word.upper()
    # 0-9
    num = [str(i) for i in range(10)]
    num = ''.join(num)

    # the whole string
    sr = word + word_up + num
"""


def code_to_file(n):
    def the_string():
        sr = string.ascii_lowercase + string.ascii_uppercase + string.digits
        return sr

    # code like tzw9-s8kK-2Jf6-p2it
    def code_gen():
        sr_result = [random.choice(the_string()) for i in range(19)]
        for i in range(1, 19):
            if i % 5 == 4:
                sr_result[i] = '-'
        code = ''.join(sr_result)
        code = code + '\n'
        return code

    # write code to code.txt
    with open('code.txt', 'w') as code_file:
        for i in range(n):
            # code_gen()
            code_file.write(code_gen())


code_to_file(10)

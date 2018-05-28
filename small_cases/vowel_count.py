# !/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    统计元音字母——输入一个字符串，统计处其中元音字母的数量。更复杂点的话统计出每个元音字母的数量。
"""


sr = 'this is a string'
lt = []
for i in sr:
    if i in 'aeiou':
        lt.append(i)
st = set(lt)
print('The count of vowel is:', len(st))


print('-' * 15)


print('The count of each vowel:')


def vowel_count():
    for i in 'aeiou':
        count = 0
        for j in lt:
            if j == i:
                count += 1
        print(i + ': ' + str(count))


vowel_count()

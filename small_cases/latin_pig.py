# !/usr/bin/env python
# -*- coding:utf-8 -*-


"""
    拉丁猪文字游戏——这是一个英语语言游戏。基本规则是将一个英语单词的第一个辅音音素的字母移动到词尾
    并且加上后缀-ay（譬如“banana”会变成“anana-bay”）。可以在维基百科上了解更多内容。
"""

sr = 'unit'

for i in sr:
    i_index = sr.index(i)
    if i not in 'aeiou':
        break
latin_sr = sr[:i_index] + sr[i_index + 1:] + '-' + i + 'ay'

print(latin_sr)

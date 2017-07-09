#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 使用 for 结构重组两个有序列表
# result = [3, 5, 6, 7, 8, 9, 10, 12, 13, 25, 30]
list1 = [3, 7, 8, 9, 12]
list2 = [5, 6, 10, 13, 25, 30]
result = []


def func(list1, list2):
    # 保证外层循环元素最多，以便最后返回拼接
    if len(list1) < len(list2):
        list1, list2 = list2, list1
    for i in list1:
        for j in list2:
            if i > j:
                # 避免内层循环重复判断
                result.append(j)
                list2 = list2[1:]
            else:
                # 因列表有序，此时 i 小于 j 及其后续所有元素，故可直接结束此轮循环
                result.append(i)
                break
            if list2 == []:
                # 此位置 i 已大于 list2 中所有元素，可跳出循环进行拼接
                temp = list1.index(i)
                break

    return result + list1[temp:]


print(func(list1, list2))

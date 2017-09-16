#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lintcode
# 6. 合并排序数组 http://www.lintcode.com/zh-cn/problem/merge-two-sorted-arrays/


# 使用 for 结构重组两个有序列表
class Solution:
    def mergeSortedArray(self, A, B):
        # write your code here
        result = []
        tt = []
        for i in A:
            for j in B:
                if i >= j:
                    # 避免内层循环重复判断
                    result.append(j)
                    B = B[1:]
                else:
                    # 因列表有序，此时 i 小于 j 及其后续所有元素，故可直接结束此轮循环
                    result.append(i)
                    A = A[1:]
                    break
            if A == []:
                tt = B
            if B == []:
                tt = A
        return result + tt


# 验证
A1 = [3, 7, 8, 9, 12]
B1 = [5, 6, 10, 13, 25, 30]
A2 = [1, 2, 3, 4]
B2 = [2, 4, 5, 6]
A3 = [7]
B3 = [5, 7]
As = [A1, A2, A3]
Bs = [B1, B2, B3]

res = Solution()
for A in As:
    for B in Bs:
        print(res.mergeSortedArray(A, B))

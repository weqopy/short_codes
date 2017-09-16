#!/usr/bin/env python
# -*- coding: utf-8 -*-

# lintcode
# 9. Fizz Buzz 问题 http://www.lintcode.com/zh-cn/problem/fizz-buzz/


result = []


class Solution:
    def fizzBuzz(self, n):
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                result.append('fizz buzz')
            elif i % 3 == 0:
                result.append('fizz')
            elif i % 5 == 0:
                result.append('buzz')
            else:
                result.append(str(i))
        return result


n = 15
res = Solution()
print(res.fizzBuzz(n))

# -------------

# A Good Answer
for i in range(1, n + 1):
    result.append('fizz'[i % 3 * 4:] + 'buzz'[i % 5 * 4:] or i)
print(result)

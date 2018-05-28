"""
141. x的平方根
实现 int sqrt(int x) 函数，计算并返回 x 的平方根。
样例
sqrt(3) = 1
sqrt(4) = 2
sqrt(5) = 2
sqrt(10) = 3
"""


# 二分法解决
class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """

    def sqrt(self, x):
        if x in (0, 1):
            return x
        l, r = 0, x
        while l <= r:
            mid = (l + r) // 2
            if mid**2 > x:
                r = mid - 1
            else:
                l = mid + 1
        return l - 1

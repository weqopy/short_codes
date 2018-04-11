"""
20.dicesSum.py
扔 n 个骰子，向上面的数字之和为 S。给定 n，请列出所有可能的 S 值及其相应的概率。
http://www.cnblogs.com/bozhou/p/6971081.html
"""


# 时间复杂度较大，待优化
class Solution:
    def getNSumCount(self, n, sum):
        if n < 1 or sum < n or sum > 6 * n:
            return 0
        elif n == 1:
            return 1
        result = (self.getNSumCount(n - 1, sum - 1) + self.getNSumCount(
            n - 1, sum - 2) + self.getNSumCount(n - 1, sum - 3) +
                  self.getNSumCount(n - 1, sum - 4) + self.getNSumCount(
                      n - 1, sum - 5) + self.getNSumCount(n - 1, sum - 6))
        return result

    def dicesSum(self, n):
        results = []
        for sum in range(n, n * 6 + 1):
            results.append([sum, round(self.getNSumCount(n, sum) / (6**n), 2)])
        return results

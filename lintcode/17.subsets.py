"""
17.subsets.py

给定一个含不同整数的集合，返回其所有的子集
子集中的元素排列必须是非降序的，解集必须不包含重复的子集
"""


class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """

    def subsets(self, nums):
        # 算法从原列表按序取值，为实现子集中元素非降序排列，首先将原列表作非降序排列处理
        nums.sort()
        result = [[]]
        for x in nums:
            result.extend([subset + [x] for subset in result])
        return result

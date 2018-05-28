# lintcode-1-A + B 问题
# http://www.lintcode.com/zh-cn/problem/a-b-problem/

lt = [2, 3, 7, 0]
target = 9


class Solution:
    """docstring for Solution"""

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        temp = {}
        for i in range(len(nums)):
            if nums[i] in temp:
                return [temp[nums[i]], i]
            else:
                temp[target - nums[i]] = i


import unittest


class testGood_Solution(unittest.TestCase):
    def test_args(self):
        self.assertFalse(Solution().twoSum([3], 4))
        self.assertEqual(Solution().twoSum([2, 3, 7, 0], 9), [0, 2])


if __name__ == '__main__':
    unittest.main()

# lintcode-1-A + B 问题
# http://www.lintcode.com/zh-cn/problem/a-b-problem/


lt = [2, 3, 7, 0]
target = 9


class Good_Solution:
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


a = Good_Solution()
# print(a.twoSum(lt, target))


class My_Solution:
    """docstring for My_Solution"""

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype:
        """
        if len(nums) <= 1:
            return False
        pass

"""
给一个包含 n 个整数的数组 S, 找到和与给定整数 target 最接近的三元组，返回这三个数的和。

 注意事项
只需要返回三元组之和，无需返回三元组本身
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target : An integer
    @return : return the sum of the three integers, the sum closest target.
    """

    def threeSumClosest(self, numbers, target):
        # write your code here
        if numbers is None or len(numbers) < 3:
            return 0
        n = len(numbers)
        numbers.sort()
        sum = 0
        for i in range(n - 1):
            left = i + 1
            right = n - 1
            while left < right:
                tmpsum = numbers[i] + numbers[left] + numbers[right]
                tmpdist = tmpsum - target
                if i == 0:
                    sum = tmpsum
                sum = sum if abs(tmpdist) > abs(sum - target) else tmpsum
                if tmpdist == 0:
                    return target
                if tmpdist < 0:
                    left += 1
                else:
                    right -= 1
        return sum

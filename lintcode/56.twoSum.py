"""
给一个整数数组，找到两个数使得他们的和等于一个给定的数 target。

你需要实现的函数twoSum需要返回这两个数的下标, 并且第一个下标小于第二个下标。注意这里下标的范围是 0 到 n-1。

你可以假设只有一组答案。
"""


class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """

    def twoSum(self, numbers, target):
        # write your code here
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i, j]

    def betterWay(self, numbers, target):
        L = {}
        result = [0, 0]
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if tmp not in L:
                L[numbers[i]] = i + 1
            else:
                result[0] = L[tmp]
                result[1] = i + 1
                break
        return result


s = Solution()
r = s.betterWay([4, 3, 7, 2], 9)
print(r)

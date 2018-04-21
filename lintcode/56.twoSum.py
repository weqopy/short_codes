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
                result[0] = L[tmp] - 1
                result[1] = i
                break
        return result


# 对于已排序整数数组，可以首尾相加，与 target 对比，较小则首下标右移，较大则尾下标左移


class Solution_2:
    def twoSum(self, numbers, target):
        if numbers is None or len(numbers) == 0:
            return None
        i = 0
        j = len(numbers) - 1
        while i < j:
            tmp = numbers[i] + numbers[j]
            if tmp < target:
                i += 1
            elif tmp > target:
                j += 1
            else:
                return [i, j]
        return None


s = Solution_2()
r = s.twoSum([2, 3, 4, 5, 7], 9)
print(r)

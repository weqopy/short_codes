"""
给一个包含n个数的整数数组S，在S中找到所有使得和为给定整数target的四元组(a, b, c, d)。

 注意事项
四元组(a, b, c, d)中，需要满足a <= b <= c <= d

答案中不可以包含重复的四元组。
"""


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array
             which gives the sum of zero
    """

    def fourSum(self, numbers, target):
        if numbers is None or len(numbers) < 4:
            return []
        result = set()
        tmpIndex = {}
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] not in tmpIndex:
                    tmpIndex[numbers[i] + numbers[j]] = [(i, j)]
                else:
                    tmpIndex[numbers[i] + numbers[j]].append((i, j))

        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                tmpNum = target - numbers[i] - numbers[j]
                if tmpNum in tmpIndex:
                    for index in tmpIndex[tmpNum]:
                        if index[0] > j:
                            result.add((numbers[i], numbers[j],
                                        numbers[index[0]], numbers[index[1]]))
        result = [list(l) for l in result]
        return result


print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

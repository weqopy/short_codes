"""
给出一个有n个整数的数组S，在S中找到三个整数a, b, c，找到所有使得a + b + c = 0的三元组。

 注意事项
在三元组(a, b, c)，要求a <= b <= c。

结果不能包含重复的三元组。
"""


class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """

    def threeSum(self, numbers):
        result = []
        if numbers is None or len(numbers) < 3:
            return result
        numbers.sort()
        n = len(numbers)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                sum = numbers[i] + numbers[left] + numbers[right]
                if sum == 0:
                    path = [numbers[i], numbers[left], numbers[right]]
                    if path not in result:
                        result.append(path)
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1

        return result


s = Solution()
print(s.threeSum([-1, 0, 1, 2, -1, -4]))

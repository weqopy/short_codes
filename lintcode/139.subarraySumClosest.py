from collections import namedtuple

Pair = namedtuple('Pair', ['sum', 'index'])


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number
             and the index of the last number
    """

    def subarraySumClosest(self, nums):
        res = []
        if not nums:
            return res

        length = len(nums)
        if length == 1:
            return [0, 0]

        sums = [Pair(0, 0)]
        prev = 0
        for i in range(1, length + 1):
            prev += nums[i - 1]
            sums.append(Pair(prev, i))

        sums = sorted(sums, key=lambda pair: pair.sum)
        import sys
        Closest = sys.maxsize
        for i in range(1, length + 1):
            sum_minus = sums[i].sum - sums[i - 1].sum
            if Closest > sum_minus:
                Closest = min(Closest, sum_minus)
                res = []
                tmp = [sums[i].index - 1, sums[i - 1].index - 1]
                tmp.sort()
                res.append(tmp[0] + 1)
                res.append(tmp[1])

        return res


arr = [-10, -2, -3, -100, 1, 2, 3, -1, 4]
res = Solution()
print(res.subarraySumClosest(arr))

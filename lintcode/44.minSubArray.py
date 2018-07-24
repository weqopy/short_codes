class Solution:
    """
    @param: nums: a list of integers
    @return: A integer indicate the sum of minimum subarray
    """

    def minSubArray(self, nums):
        ln = len(nums)

        if ln == 0:
            return 0

        min = nums[0]
        for i in nums[1:]:
            if i < min:
                min = i
        if min > 0:
            return min

        dp = 0
        res = 0
        for j in nums:
            dp += j
            if dp > 0:
                dp = 0
            elif dp < res:
                res = dp

        return res


res = Solution()
array = [-2, 2, -3, 4, -1, 2, 1, -5, 3]

print(res.minSubArray(array))

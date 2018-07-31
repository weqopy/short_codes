class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """

    def maxSubArray(self, nums):
        ln = len(nums)
        start, end = 0, 0

        if ln == 0:
            return 0

        dp = [0] * ln
        dp[0] = nums[0]
        MaxSumSub = dp[0]

        tmp = 0

        for i in range(1, ln):
            if dp[i - 1] <= 0:
                dp[i] = nums[i]
                tmp = i
            else:
                dp[i] = nums[i] + dp[i - 1]

            if dp[i] > MaxSumSub:
                MaxSumSub = dp[i]
                start, end = tmp, i
        return MaxSumSub

    def maxSubArray_dp(self, nums):
        ln = len(nums)
        start, end = 0, 0

        if ln == 0:
            return 0

        dp = [nums[0]] + [0] * (ln - 1)

        for i in range(1, ln):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)


res = Solution()
array = [-2, 2, -3, 4, -1, 2, 1, -5, 3]

print(res.maxSubArray(array))
print(res.maxSubArray_dp(array))

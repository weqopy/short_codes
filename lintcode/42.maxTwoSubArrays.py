class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """

    def maxSubArray_dp(self, ln, nums):
        dp = nums[0]

        for i in range(1, ln):
            dp = max(dp + nums[i], nums[i])
        return dp

    def maxTwoSubArrays(self, nums):
        ln = len(nums)
        if ln == 0:
            return 0
        elif ln == 1:
            return nums

        temp = -65535
        for i in range(1, ln):
            left_max = self.maxSubArray_dp(i, nums[:i])
            right_max = self.maxSubArray_dp(ln - i, nums[i:])
            temp = max(temp, left_max + right_max)
        return temp


res = Solution()
array = [0, -1]

print(res.maxTwoSubArrays(array))

class Solution1:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # O(n^2)
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        max_tmp = 1

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                max_tmp = max(max_tmp, dp[i])
        return max_tmp


class Solution2:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """

    # O(nlogn)
    def longestIncreasingSubsequence(self, nums):
        if len(nums) == 0:
            return 0
        stack = [nums[0]]
        for i in nums[1:]:
            size = len(stack)
            if i > stack[size - 1]:
                stack.append(i)
            elif i < stack[size - 1]:
                index = self.binarysearchlarger(stack, i)
                stack[index] = i
        return len(stack)

    def binarysearchlarger(self, stack, target):
        left, right = 0, len(stack) - 1
        while left <= right:
            mid = (left + right) // 2
            if stack[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left


nums = [10, 1, 11, 2, 12, 3, 11]
res = Solution2()
print(res.longestIncreasingSubsequence(nums))

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """

    def binarySearch(self, nums, target):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                if nums[mid - 1] < target:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1

        if nums[left] == target:
            return left

        return -1


nums = [1, 4, 4, 5, 6, 6, 8, 9, 9, 10]
result = Solution()
for i in [1, 2, 4, 6, 7, 9]:
    print(result.binarySearch(nums, i), end=' ')  # 0 -1 1 4 -1 7

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        # write your code here
        if nums is None:
            return None
        elif nums == []:
            return 0

        left = []
        right = []
        for i in nums:
            if i < k:
                left.append(i)
            else:
                right.append(i)

        return len(left)

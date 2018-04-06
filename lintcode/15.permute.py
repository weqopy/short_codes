"""
全排列：给定一个数字列表，返回其所有可能的排列。
递归、迭代算法
"""


class Solution_1:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):
        # write your code here
        res = []

        def helper(res, l, r, n, max):
            if n == max:
                # print(l)
                res.append(l)
            for i in range(0, len(r)):
                helper(res, l + [r[i]], r[:i] + r[i + 1:], n + 1, max)

        helper(res, [], nums, 0, len(nums))
        return res


class Solution_2:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """

    def permute(self, nums):

        if len(nums) <= 1:
            return [nums]
        output = [[nums[0], nums[1]], [nums[1], nums[0]]]
        for i in range(2, len(nums)):
            tmp = nums[i]
            output_new = []
            for j in range(len(output)):
                output[j].append(tmp)
                output_new.append(output[j])
                for k in range(len(output[j]) - 1):
                    line = [n for n in output[j]]
                    line[len(line) - 1], line[k] = line[k], tmp
                    output_new.append(line)
            output = output_new
        return output


nums = [1, 2, 3, 4]

result = Solution_2()
r = result.permute(nums)
print(r)

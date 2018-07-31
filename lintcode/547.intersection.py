class Solution:

    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """

    def intersection_1(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection_2(self, nums1, nums2):
        # 耗时
        res = []
        for i in nums1:
            if i in res:
                continue
            for j in nums2:
                if i == j and j not in res:
                    res.append(j)
        return res

    def intersection_3(self, nums1, nums2):
        # 使用字典，用时较少
        tmp = {}
        for i in nums1:
            if i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
        for j in nums2:
            if j in tmp:
                tmp[j] = 0
        return [k for k in tmp if tmp[k] == 0]

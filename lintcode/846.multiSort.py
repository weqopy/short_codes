class Solution:
    def multiSort(self, array):
        dic = {}
        for arr in array:
            if arr[1] in dic:
                dic[arr[1]].append(arr[0])
                dic[arr[1]].sort()
            else:
                dic.update({arr[1]: [arr[0]]})
        od = sorted(dic.keys(), reverse=True)
        ans = []
        for key in od:
            for ids in dic[key]:
                ans.append([ids, key])
        return ans


array = [[2, 50], [1, 50], [3, 100]]
res = Solution()
print(res.multiSort(array))

# lintcode-55-比较字符串
# http://www.lintcode.com/zh-cn/problem/compare-strings/#


class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """

    def compareStrings(self, A, B):
        # all 语句在 B 中有重复字符时仍然返回 True
        # return all(i in A for i in B)

        # 通过字典计数
        if len(A) < len(B):
            return False
        if len(B) == 0 or B is None:
            return True
        d = {}
        for a in A:
            if a not in d:
                d[a] = 1
            else:
                d[a] += 1
        for b in B:
            if b not in d:
                return False
            else:
                d[b] -= 1
                if d[b] < 0:
                    return False
        return True


A = "ABCDEFG"
B = "ACC"
res = Solution()
print(res.compareStrings(A, B))

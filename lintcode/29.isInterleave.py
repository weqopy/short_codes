class Solution:
    """
    @params s1, s2, s3: Three strings as description.
    @return: return True if s3 is formed by the interleaving of
             s1 and s2 or False if not.
    @hint: you can use [[True] * m for i in range (n)] to allocate a n*m matrix
    """

    def isInterleave(self, s1, s2, s3):
        # 动态规划，dp
        len1 = 0 if s1 is None else len(s1)
        len2 = 0 if s2 is None else len(s2)
        len3 = 0 if s3 is None else len(s3)

        if len3 != len1 + len2:
            return False

        f = [[False] * (1 + len2) for i in range(1 + len1)]
        f[0][0] = True
        for i in range(1, 1 + len1):
            # f[i][0] = s1[i - 1] == s3[i - 1] and f[i - 1][0]
            # s2 为空字符串时，直接对比 s1 s3 前 i 位
            f[i][0] = s1[:i] == s3[:i]
        for i in range(1, 1 + len2):
            # f[0][i] = s2[i - 1] == s3[i - 1] and f[0][i - 1]
            # s1 为空字符串时，直接对比 s2 s3 前 i 位
            f[0][i] = s2[:i] == s3[:i]

        for i1 in range(1, 1 + len1):
            for i2 in range(1, 1 + len2):
                case1 = s1[i1 - 1] == s3[i1 + i2 - 1] and f[i1 - 1][i2]
                case2 = s2[i2 - 1] == s3[i1 + i2 - 1] and f[i1][i2 - 1]
                f[i1][i2] = case1 or case2

        return f[len1][len2]

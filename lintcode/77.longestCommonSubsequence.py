class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        d = [[0]*(len(B)+1) for i in range(len(A)+1)]

        for i in range(1, len(A)+1):
            for j in range(1, len(B)+1):
                if A[i-1] == B[j-1]:
                    d[i][j] = d[i-1][j-1]+1
                else:
                    d[i][j] = max(d[i - 1][j], d[i][j - 1])
        return d[-1][-1]


s1 = [1, 3, 4, 5, 6, 7, 7, 8]
s2 = [3, 5, 7, 4, 8, 6, 7, 8, 2]

res = Solution()
print(res.longestCommonSubsequence(s1, s2))

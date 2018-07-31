class Solution:
    def backPack(self, m, A):
        #  TODO: 出现 Memory Limit Exceede 情况
        n = len(A)
        dp = [[0 for col in range(m + 1)] for raw in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if j >= A[i - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i - 1]] + A[i - 1])
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]

    def backPack_2(self, m, A):
        #  好的解法
        n = len(A)
        dp = [0 for x in range(m + 1)]
        dp[0] = 1
        ans = 0
        for item in A:
            for i in range(m, -1, -1):
                if i - item >= 0 and dp[i - item] > 0:
                    ans = max(ans, i)
                    dp[i] = 1
        return ans


A = [2, 3, 5, 7]
m = 11
res = Solution()
print(res.backPack(m, A))

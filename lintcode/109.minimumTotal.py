class Solution:
    """
    @param triangle: a list of lists of integers
    @return: An integer, minimum path sum
    """

    def minimumTotal(self, triangle):
        # write your code here
        n = len(triangle)
        f = [[None] * n] * n

        f[n - 1] = triangle[n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(0, i + 1):
                f[i][j] = min(f[i + 1][j], f[i + 1][j + 1]) + triangle[i][j]

        return f[0][0]

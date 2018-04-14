class Solution:
    """
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """

    def searchMartix(self, martix, target):
        m = len(martix)
        for i in range(m):
            if martix[i][0] == target:
                return True
            # 非首行的首位元素大于目标值，则目标如存在，必在该行前一行
            elif martix[i][0] > target and i >= 1:
                for j in martix[i - 1]:
                    if j == target:
                        return True
        return False


lt = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
s = Solution()
print(s.searchMartix(lt, 1))

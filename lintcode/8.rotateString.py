"""
旋转字符串
http://www.lintcode.com/zh-cn/problem/rotate-string/
"""


class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    暴力方法，时间复杂度为O(m * n)，空间复杂度为O(1)
    """

    def rotateString(self, str, offset):
        offset %= len(str)
        while offset > 0:
            self.rotate(self, str)
            offset -= 1
        return str

    def rotate(self, str):
        g = str[-1]
        str = g + str[:-1]


class GoodSolution:
    """
    三步反转
    时间复杂度为O(n)，空间复杂度为O(1)
    """

    def rotateString(self, sr, offset):
        offset %= len(sr)
        left = 0
        right = len(sr) - 1
        # 将字符串转换为列表，以方便元素换位
        sr = list(sr)
        self.rotate(sr, 0, right - offset)
        self.rotate(sr, right - offset + 1, right)
        self.rotate(sr, 0, right)
        return ''.join(sr)

    def rotate(self, sr, left, right):
        while left < right:
            sr[left], sr[right] = sr[right], sr[left]
            left += 1
            right -= 1


s = GoodSolution()
lt = 'abcdefg'
print(s.rotateString(lt, 3))

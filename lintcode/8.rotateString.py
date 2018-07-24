"""
旋转字符串
http://www.lintcode.com/zh-cn/problem/rotate-string/
"""


class Solution:
    """
    三步反转
    时间复杂度为O(n)，空间复杂度为O(1)
    """

    def rotateString(self, str, offset):
        l = len(str)
        return str[l-offset:]+str[0:l-offset]

    def rotate(self, sr, left, right):
        while left < right:
            sr[left], sr[right] = sr[right], sr[left]
            left += 1
            right -= 1


s = Solution()
lt = 'abcdefg'
print(s.rotateString(lt, 3))

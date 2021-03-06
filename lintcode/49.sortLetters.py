"""
给定一个只包含字母的字符串，按照先小写字母后大写字母的顺序进行排序。

 注意事项
小写字母或者大写字母他们之间不一定要保持在原始字符串中的相对位置。
"""


class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, chars):
        # write your code here
        import string
        lowercase = []
        uppercase = []
        for i in chars:
            if i in string.ascii_lowercase:  # a-z
                lowercase.append(i)
            elif i in string.ascii_uppercase:  # A-Z
                uppercase.append(i)
        return ''.join(lowercase + uppercase)


class newSolution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """

    def sortLetters(self, str):
        import string

        low = string.ascii_lowercase
        up = string.ascii_uppercase

        left = 0
        right = len(str) - 1
        lt = list(str)
        while left < right:
            while left < right and lt[left] in low:
                left += 1
            if left < right:
                lt[left], lt[right] = lt[right], lt[left]
                right -= 1

            while left < right and lt[right] in up:
                right -= 1
            if left < right:
                lt[left], lt[right] = lt[right], lt[left]
                left += 1
        return ''.join(lt)

"""
反转一个只有3位数的整数。

注意事项
你可以假设输入一定是一个只有三位数的整数，这个整数大于等于100，小于1000。
"""


class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """

    def reverseInteger(self, number):
        # write your code here
        a, b, c = [str(number)[i] for i in range(3)]
        if number % 100 == 0:
            return int(a)
        elif number % 10 == 0:
            return int(b + a)
        else:
            return int(c + b + a)

class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """

    def nthUglyNumber(self, n):
        if n > 1:
            number = [1]
            i2, i3, i5 = 0, 0, 0
            for i in range(1, n - 1):
                n2, n3, n5 = number[i2] * 2, number[i3] * 3, number[i5] * 5
                Min = min(n2, n3, n5)
                number.append(Min)
                i2 += (Min == n2)
                i3 += (Min == n3)
                i5 += (Min == n5)
            return Min
        elif n == 1:
            return 1
        else:
            return 0

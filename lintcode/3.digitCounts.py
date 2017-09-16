# lintcode-3-统计数字
# http://www.lintcode.com/zh-cn/problem/digit-counts/


class Solution:
    def digitCounts(self, k, n):
        count = 0
        # n 的位数
        ln = len(str(n))
        for i in range(1, ln + 1):
            # k 为 0 时，首位可跳过
            # k 为 0 的处理待完善
            if k == 0:
                if n >= 0 and n < 10:
                    count = 1
                if i == ln:
                    break
            a = n // (10 ** i) * (10 ** (i - 1))

            n_i = n % (10 ** i) // (10 ** (i - 1))
            if n_i > k:
                num = a + 10 ** (i - 1)
            elif n_i < k:
                num = a
            elif n_i == k:
                num = a + 1 + n % (n_i * (10 ** (i - 1)))
            count += num
        return count


# 验证
lt = [0, 9, 35, 99, 999, 2593]
ks = [0, 5]

res = Solution()
for k in ks:
    for n in lt:
        print(res.digitCounts(k, n))

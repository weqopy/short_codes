# lintcode-13-字符串查找
# http://www.lintcode.com/zh-cn/problem/strstr/


class Solution:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        current, index = 0, 0
        ln_s = len(source)
        ln_t = len(target)
        while current <= ln_s - ln_t:
            temp = current
            while index != ln_t:
                if target[index] != source[current]:
                    break
                else:
                    index += 1
                    current += 1
            if index == ln_t:
                return current - ln_t
            current = temp + 1
            index = 0
        return -1


source = "tartarget"
target = "target"
res = Solution()
print(res.strStr(source, target))

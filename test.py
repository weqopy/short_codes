def reverse_str(base_num):
    num_str = str(base_num)
    reverse_str = "".join(reversed(num_str))
    if num_str == reverse_str:
        return [True, base_num]
    else:
        new_num = base_num + int(reverse_str)
        return [False, new_num]


num = 345
i = 0
while True:
    res, new_num = reverse_str(num)
    print([i, num, res, new_num])
    if res:
        print(i, new_num)
        break
    else:
        num = new_num
    i += 1

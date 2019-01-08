mt = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def deform_matrix(mt):

    print("左上右下为轴翻转: {}".format(list(map(list, zip(*mt)))))
    print("左下右上为轴翻转: {}".format(list(map(list, zip(*mt[::-1])))[::-1]))
    print("顺时针旋转: {}".format(list(map(list, zip(*mt[::-1])))))
    print("逆时针旋转: {}".format(list(map(list, zip(*mt)))[::-1]))


def clockwisely(mt):
    """print matrix clockwisely"""
    res = []
    while mt:
        res.extend(mt[0])
        mt.pop(0)
        mt = list(map(list, zip(*mt)))[::-1]
    return "旋转打印矩阵: {}".format(res)


deform_matrix(mt)
print("*" * 10)
print(clockwisely(mt))

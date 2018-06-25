"""
https://github.com/Yixiaohan/show-me-the-code
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示：

{
	"1":["张三",150,120,100],
	"2":["李四",90,99,95],
	"3":["王五",60,66,68]
}
"""


def get_list_student():
    import json

    with open('./student.txt', 'r') as f:
        data = json.load(f, encoding='utf-8')
    res = []
    for k, v in data.items():
        tmp = []
        tmp.append(k)
        for j in v:
            tmp.append(str(j))
        res.append(tmp)
    return res


def write_to_excel(lists):
    from openpyxl import Workbook
    wb = Workbook()

    ws = wb.active
    for i in lists:
        ws.append(i)

    wb.save('student.xlsx')


if __name__ == '__main__':
    lists = get_list_student()
    write_to_excel(lists)

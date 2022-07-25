import requests
from rich import print
from lxml import etree
from time import sleep
import pandas as pd

base_url = "http://218.28.223.13/zzzfdc/zhengzhou/prelicence_later.jsp?presale_number="
list_file = "zz_list.csv"

def get_item_data(code):
    url = base_url + str(code)
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)

    arr = []
    try:
        table = tree.xpath('//*/table')[4].xpath('.//tr//td/text()')
        for item in table:
            item = item.replace("\xa0","").replace("\r\n","").replace(" ","")
            arr.append(item)
    except:
        return [None, True]

    if len(arr) == 0:
        return [None, True]
    else:
        return [arr, False]


def main():
    arr = []
    error_pages = []
    df = pd.read_csv(list_file)
    codes = df['代码']
    for code in codes:
        item_row, error = get_item_data(code)
        if error:
            pass
        else:
            arr.append(item_row)
            save_data(arr)
    # return arr

def save_data(arr):
    # columns = "公司名称,代码,项目名称,地址"
    result = pd.DataFrame(
        arr,
    )
    result.to_csv("zz_item.csv", index=False)

if __name__ == '__main__':
    main()
    # save_data(arr)


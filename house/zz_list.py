import requests
from rich import print
from lxml import etree
from time import sleep
import pandas as pd

base_url = "http://218.28.223.13/zzzfdc/zhengzhou/permission.jsp?pn=&cn=&it=&pager.offset=0&page="

def get_page_data(page_num):
    url = base_url + str(page_num)
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers)
    tree = etree.HTML(res.text)

    arr = []
    try:
        data = tree.xpath('//*/form[@id="searchform"]/table//tr')
    except:
        return [None, True]


    for element in data:
        try:
            item = element.xpath(f'.//td/text()')
            company_name = element.xpath(f'.//a/text()')
            if len(item) == 0:
                continue
            arr.append(company_name + item)
        except:
            continue
    
    if len(arr) == 0:
        return [None, True]
    else:
        return [arr, False]


def main(total_page):
    arr = []
    error_pages = []

    for page in range(1, total_page):
        print(f'正在爬取第{page}页')
        sleep(2)
        page_arr, error = get_page_data(page)
        print(page_arr)
        if page_arr is not None:
            arr += page_arr
        print(arr)
        print('-------')

        if error:
            error_pages.append(page)

    return [arr, error_pages]

def save_data(arr, filename, columns):
    result = pd.DataFrame(
        arr,
        columns=columns.split(","),
    )
    result.to_csv(f"{filename}.csv", index=False)

if __name__ == '__main__':
    total_page = 3
    arr, error_pages = main(total_page)
    save_data(arr, 'zz_list', "公司名称,代码,项目名称,地址")
    save_data(error_pages, 'error_pages', 'page')

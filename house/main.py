import time, math
import requests
from lxml import html


def get_item(item):
    name = item.xpath("./div/div[1]/a/@title")[0]
    url = homepage_url + item.xpath("./div/div[1]/a/@href")[0]
    print([name, url])

    address = item.xpath("./div/a[1]/text()")[1].strip()
    city_area = address.split("/")[0]

    area_type = item.xpath("./div/a[2]/span[2]/text()")[0]
    area_str = item.xpath("./div/a[2]/span[last()]/text()")[0]
    area = area_str.replace("建面 ", "").replace("㎡", "")

    price = item.xpath("./div/div[4]/div[1]/span[1]/text()")[0]
    total_str = item.xpath("./div/div[4]/div[2]/text()")[0]
    total = total_str.replace("总价", "").replace("(万/套)", "")

    arr = [name, url,city_area, address, area_type, area, price, total]
    return arr


def get_error_item(item):
    name = item.xpath("./div/div[1]/a/@title")[0]
    url = homepage_url + item.xpath("./div/div[1]/a/@href")[0]

    return [name, url]


def get_total_page():
    res = requests.get(init_url)
    res.encoding = "utf-8"
    tree = html.fromstring(res.text)
    count_str = tree.xpath("/html/body/div[7]/div[2]/@data-total-count")[0]
    count = int(count_str)
    total_page = math.ceil(count / 10)
    return total_page


def get_data(data_type, total_page):
    data = []
    error_data = []
    for j in range(1, total_page + 1):
        if data_type == 0:
            # page_url reason
            # 替换页码，不同城市、筛选条件的地址可能不同，pgn 出现位置不同
            # 默认筛选条件后 pg1 不出现，需切换页码后出现
            page_url = init_url.replace("pg2", f"pg{j}")
            time.sleep(3)
            headers = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
            }
            res = requests.get(page_url, headers=headers)
            res.encoding = "utf-8"
            tree = html.fromstring(res.text)
        else:
            file_content = ""
            try:
                with open(f"house/pages/page{j}.html") as f:
                    file_content = f.read()
                tree = html.fromstring(file_content)
            except:
                continue

        lists = tree.xpath("/html/body/div[6]/ul[2]/li")
        for i in range(len(lists)):
            item = lists[i]
            try:
                arr = get_item(item)
                data.append(arr)
            except:
                error_str = get_error_item(item)
                error_info = (
                    f"error in page {j}, item {i+1}, {error_str[0]}, {error_str[1]}"
                )
                error_data.append(error_info)
                print(error_info)
                continue
    return [data, error_data]


def write_data_to_file(data, error_data):
    with open("house/house_data.txt", "w", encoding="utf-8") as target:
        for da in data:
            target.write(str(da) + "\n")
        target.write("-----------------\n")
        for da in error_data:
            target.write(str(da) + "\n")


if __name__ == "__main__":
    total_page = 99
    # 运行方式，爬虫抓取-0/读取本地文件-1
    # 爬虫抓取可能出现错误数据（页面实际不存在的数据、乱序等）
    data_type = 1
    # 设置好筛选条件，在下面页码列表点到后续第 2 页地址，原因见 get_data 函数 page_url reason 注释
    init_url = ""
    # 首页网址，用于拼接楼盘页面地址
    homepage_url = init_url.split("/loupan")[0]
    if data_type == 0:
        total_page = get_total_page()
    print(homepage_url)
    data, error_data = get_data(data_type, total_page)
    write_data_to_file(data, error_data)

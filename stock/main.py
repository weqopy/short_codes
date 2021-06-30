import requests
from lxml import html

base_url = "https://xueqiu.com/S/"

stocks = ["601636.SH"]  # , "000949.SZ"]

res = []
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"
}
for stock in stocks:
    url_expand = stock.split(".")
    url = base_url + url_expand[1] + url_expand[0]
    res = requests.get(
        url,
        headers=headers,
    )

    tree = html.fromstring(res.text)

    current = tree.xpath(
        '//*[@id="app"]/div[2]/div[2]/div[5]/div/div[1]/div[1]/strong/text()'
    )

    with open("stock/test.txt", "w", encoding="utf-8") as target:
        target.write(res.text)


# ----------------------------------------------------------------

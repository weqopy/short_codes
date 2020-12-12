import os
from lxml import etree


def get_source_data(filepath):
    if not os.path.exists(filepath):
        return None
    file = open(filepath)
    sel = etree.HTML(file.read())

    group_titles = sel.xpath("/html/body/dl/dt")
    hash = {}
    for i, group_items in enumerate(group_titles):
        group_title = group_items.xpath("./h3/text()")[0]
        temp = []

        i += 1
        items = sel.xpath(f"/html/body/dl/dl[{i}]//dt")
        for item in items:
            url = item.xpath("./a/@href")[0]
            title = item.xpath("./a/text()")[0]
            temp.append({"url": url, "title": title})
        hash[group_title] = temp
    return hash

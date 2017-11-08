import requests
from lxml import html


class Spider(object):
    result = {}
    page = 1
    basic_url = 'https:'
    URL = 'https://www.qidian.com/all?chanId=5&subCateId=22&orderId=&page=1&style=1&pageSize=20&siteid=1&pubflag=0&hiddenField=0'

    def get_tree(self, URL):
        # global URL
        response = requests.get(self.URL)
        response.encoding = 'utf-8'
        tree = html.fromstring(response.text)
        # print('网页标题显示测试:')
        # print(tree.xpath('//head/title/text()')[0])
        return tree

    def get_current_page(self):
        tree = self.get_tree(self.URL)
        current_book_count = len(tree.xpath('//li[@data-rid]'))
        current_page_book_name = tree.xpath('//ul/li/div[2]/h4/a/text()')
        current_page_book_url = tree.xpath('//ul/li/div[2]/h4/a/@href')
        current_page_book_author = tree.xpath('//ul/li/div[2]/p/a[1]/text()')
        for id in range(1, current_book_count + 1):
            book = current_page_book_name[id - 1] + '-' + current_page_book_author[id -
                                                                                   1] + '-' + self.basic_url + current_page_book_url[id - 1]
            self.result[str(self.page) + '_' + str(id)] = book
        return self.result

    def get_next_page_url(self):
        tree = self.get_tree(self.URL)
        next_url = self.basic_url + \
            tree.xpath(
                '//ul/li[@class="lbf-pagination-item"]/a[text()=">"]/@href')[0]
        self.get_current_page()
        self.URL = next_url
        self.page += 1

    def write_in_file(self):
        import json
        result = self.get_current_page()
        data = json.dumps(result, ensure_ascii=False)
        with open('qidian_books.txt', 'w', encoding='utf-8') as target:
            target.write(data)

    def basic(self):
        for i in range(3):
            self.write_in_file()


if __name__ == '__main__':
    sp = Spider()
    sp.write_in_file()

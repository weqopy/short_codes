import requests
from lxml import html
import os

URL_LOGIN = 'https://github.com/login'
URL_SESSION = 'https://github.com/session'

ss = requests.Session()
resp = ss.get(URL_LOGIN)
tree = html.fromstring(resp.text)
authenticity_token = tree.xpath('//*[@id="login"]/form/div[1]/input[2]/@value')
password = os.environ.get('Github_Password')

data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': 'weqopy@gmail.com',
    'password': password
}

resp_2 = ss.post(URL_SESSION, data=data)
tree_2 = html.fromstring(resp_2.text)
# repo_name = tree_2.xpath('//*[@id="your_repos"]/div/div[2]/ul/li[1]/a/span/span/text()')
repo_name = tree_2.xpath(
    '//li[@class="public source"]//span[@class="repo"]/text()')

print(repo_name)

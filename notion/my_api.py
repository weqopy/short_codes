import requests
import json
import time

url = "https://api.notion.com/v1/pages"
token = ""
database_id = ""
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13",
}
title = "notion api 可以使用"
content = "ccccccc"

data = {
    "parent": {"database_id": database_id},
    "properties": {
        "Name": {"title": [{"text": {"content": title}}]},
    },
    "children": [
        {
            "object": "block",
            "type": "paragraph",
            "paragraph": {"text": [{"text": {"content": content}}]},
        },
    ],
}
# print(headers)
# print(data)
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.status_code)
if r.status_code != 200:
    res = json.loads(r.text)
    print(res["message"])

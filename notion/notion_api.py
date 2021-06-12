from notion.client import NotionClient
from notion.block import TextBlock

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
client = NotionClient(token_v2="")

# Replace this URL with the URL of the page you want to edit
url = "https://www.notion.so/notion_api-1003f63ca2a543cf8adef2e447ef0824"
page = client.get_block(url)

print("The old title is:", page.title)

# Note: You can use Markdown! We convert on-the-fly to Notion's internal formatted text data structure.
new_title = "notion_api"
page.title = new_title
# print("The new title is:", new_title)

newchild = page.children.add_new(TextBlock, title="Something text")
# newchild.checked = True

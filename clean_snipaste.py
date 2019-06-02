import os, shutil
from datetime import datetime

user_name = os.environ.get("USER_NAME")
folder = user_name + "Pictures/Snipaste/"
trash = user_name + "trash/"

now = datetime.today()
for item in os.listdir(folder):
    item_stats = os.stat(folder + item)
    create_time = datetime.fromtimestamp(item_stats.st_mtime)
    if (now - create_time).days > 30:
        shutil.move(folder + item, trash)

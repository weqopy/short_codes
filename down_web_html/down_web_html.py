import os, sys, time
import shutil
from selenium import webdriver
import pyautogui, eventlet
from get_source_data import get_source_data
import pyperclip


pyautogui.PAUSE = 0.5

def get_downloaded_urls(downloaded_file):
    urls = []
    if os.path.exists(downloaded_file):
        with open(downloaded_file, "r") as f:
            for line in f.readlines():
                urls.append(line.rstrip())
    return urls

def main(source_data, downloaded_urls, crx_files):
    options = webdriver.ChromeOptions()
    # 无效设置
    # user_name = os.environ.get("USER_NAME")
    # out_path = f"{user_name}/Downloads/down_test"
    # prefs = {'download.default_directory': out_path}
    # prefs = {'profile.default_content_setting_values' :  {'notifications' :2}}
    # options.add_experimental_option('prefs', prefs)
    # headless 模式下无法调用 add_extension
    # options.add_argument('--headless')
    for crx in crx_files:
        options.add_extension(crx)
    eventlet.monkey_patch()

    driver = webdriver.Chrome(options=options)
    # pyautogui.hotkey('commacd', 'w') 无效
    pyautogui.keyDown('command')
    pyautogui.keyDown('w')
    pyautogui.keyUp('command')
    pyautogui.keyUp('w')
    time.sleep(1)
    flag = True
    for group_title, data in source_data.items():
        for item in data:
            url = item.get("url")
            if url is None or url in downloaded_urls:
                continue
            title = item.get("title")
            try:
                print(f"downloading {url}")
                with eventlet.Timeout(5, False):
                    driver.get(url)
                down_num = 20
                if "www.zhihu.com" in url:
                    pyautogui.hotkey("esc")
                    down_num = 50
                for i in range(down_num):
                    pyautogui.hotkey('pagedown')
                # save
                pyautogui.keyDown('command')
                pyautogui.keyDown('s')
                pyautogui.keyUp('command')
                pyautogui.keyUp('s')
                time.sleep(1)
                # paste title
                pyperclip.copy("_".join([group_title, title]))
                pyautogui.keyDown('command')
                pyautogui.keyDown('v')
                pyautogui.keyUp('command')
                pyautogui.keyUp('v')
                # pyautogui.typewrite(title)
                if flag:
                    for i in range(8):
                        pyautogui.hotkey('tab')
                    pyautogui.hotkey('space')
                    pyautogui.hotkey('up')
                    pyautogui.hotkey('enter')
                    flag = False
                pyautogui.hotkey('enter')
                time.sleep(1)
                pyautogui.hotkey('space')
                time.sleep(5)
                with open("downloaded_url.txt", "a") as f:
                    f.write(url + "\n")
            except Exception as e:
                raise e
    driver.close()


if __name__ == "__main__":
    cwd = os.path.split(os.path.realpath(__file__))[0]
    downloaded_file = f"{cwd}/downloaded_url.txt"
    downloaded_urls = get_downloaded_urls(downloaded_file)
    args = sys.argv
    if len(args) == 1:
        user_name = os.environ.get("USER_NAME")
        source_file = f"{user_name}/Downloads/Raindrop.io.html"
    else:
        source_file = sys.argv[1]
    source_data = get_source_data(source_file)
    if source_data is None:
        print(f"{source_file} 文件异常，无法获取源数据。")
    else:
        crx_files = [f"{cwd}/AdBlock_4.24.1_0.crx"]
        print(f"args--source_file:{source_file}--downloaded_file:{downloaded_file}--crx_files:{crx_files}")
        main(source_data, downloaded_urls, crx_files)

    download_path = f"{user_name}/Downloads"
for item in os.listdir(download_path):
    item_path = f"{download_path}/{item}"
    if ".mhtml" in item_path:
        shutil.move(item_path, f"{user_name}/Documents/web_html/")
    elif item == "Raindrop.io.html":
        shutil.move(item_path, cwd)

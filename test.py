import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from helium import *
import pyautogui


pyautogui.PAUSE = 2

try:
    start_chrome("http://www.baidu.com/")
    pyautogui.hotkey('command', 's')
    pyautogui.write('ood')
    pyautogui.hotkey('enter')
except Exception as e:
    raise e
finally:
    kill_browser()

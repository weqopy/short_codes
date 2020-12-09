import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


try:
    browser = webdriver.Chrome()
    browser.get('http://www.baidu.com/')
    time.sleep(1)
    print("opened...")
    ActionChains(browser).key_down(Keys.COMMAND).send_keys('s').key_up(Keys.COMMAND).perform()
    # browser.find_element_by_id('body').send_keys(Keys.COMMAND,'s')
    time.sleep(1)
    ActionChains(browser).send_keys(Keys.ENTER).perform()
    # browser.find_element_by_id('body').send_keys(Keys.ENTER)
    time.sleep(1)
except Exception as e:
    raise e
finally:
    browser.quit()

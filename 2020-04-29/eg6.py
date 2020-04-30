from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://127.0.0.1/biz/user-login.html")

# 键盘键的相关操作
time.sleep(4)
driver.find_element_by_id("account").clear()
time.sleep(4)
driver.find_element_by_id("account").send_keys("admin")
driver.find_element_by_id("account").send_keys(Keys.TAB)
time.sleep(6)
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("chandao0325")
driver.find_element_by_name("password").send_keys(Keys.ENTER)
time.sleep(6)
driver.quit()
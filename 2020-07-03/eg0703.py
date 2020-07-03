from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")


driver.find_element_by_id("kw").send_keys("字节跳动")
time.sleep(5)
driver.find_element_by_id("su").click()
time.sleep(5)
driver.quit()
from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('checkbox.html')
driver.get(file_path)

# 定位一组元素

inputs = driver.find_elements_by_tag_name("input") #注意此处定位多个元素需要用elements
# python的循环结构格式
for input in inputs:
    if input.get_attribute('type') == 'checkbox':
        input.click()
time.sleep(2)
driver.quit()
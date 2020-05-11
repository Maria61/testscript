from selenium import webdriver
import time
import os

# 文件上传操作

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('upload.html')
driver.get(file_path)
time.sleep(4)

driver.find_element_by_tag_name("input").send_keys('E://learningcode//testscript//2020-05-11//modal.html')


time.sleep(4)
driver.quit()
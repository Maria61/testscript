from selenium import webdriver
import time
import os

# div对话框的处理

driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('modal.html')
driver.get(file_path)
time.sleep(4)

driver.find_element_by_id("show_modal").click()
time.sleep(4)
driver.find_element_by_link_text("click me").click()
time.sleep(4)
buttons = driver.find_elements_by_tag_name("button")
buttons[1].click()
driver.find_element_by_link_text("Click").click()
time.sleep(4)
# driver.find_element_by_class_name("modal-footer")
driver.find_element_by_xpath("//*[@id='myModal']/div[3]/button[1]").click()

time.sleep(4)
driver.quit()

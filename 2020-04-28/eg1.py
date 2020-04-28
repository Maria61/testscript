from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# driver.find_element_by_id("kw").send_keys("大虞海棠")
# driver.find_element_by_class_name("s_ipt").send_keys("大虞海棠")
# driver.find_element_by_name("wd").send_keys("大虞海棠")
# time.sleep(6)
# driver.find_element_by_id("su").click()
# driver.find_element_by_class_name("btn self-btn bg s_btn").click() #无法定位到该元素
# driver.find_element_by_id("su").click()
# driver.find_element_by_link_text("抗击肺炎").click()
driver.find_element_by_partial_link_text("肺炎").click()
time.sleep(8)
driver.quit()
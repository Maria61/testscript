from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 练习定位元素

# 通过id定位元素
# driver.find_element_by_id("kw").send_keys("大虞海棠")
# 通过class定位元素
# driver.find_element_by_class_name("s_ipt").send_keys("大虞海棠")
# 通过name定位元素
# driver.find_element_by_name("wd").send_keys("大虞海棠")
# time.sleep(6)
# driver.find_element_by_id("su").click()
# 由于该元素对应的class_name不是唯一的(一个空格间隔一个class的name)，有btn，self-btn，bg ，s_btn，无法定位到该元素
# driver.find_element_by_class_name("btn self-btn bg s_btn").click()
# driver.find_element_by_id("su").click()
# 通过文字链接定位元素
# driver.find_element_by_link_text("抗击肺炎").click()
# 通过部分文字链接定位元素
# driver.find_element_by_partial_link_text("肺炎").click() #要保证页面元素的唯一性，否则无法定位到
# 通过xpath定位元素
# driver.find_element_by_xpath("//*[@id='kw']").send_keys("Lisa")
# driver.find_element_by_xpath("//*[@id='su']").click()
# 通过css定位元素
driver.find_element_by_css_selector("#kw").send_keys("Lisa")
driver.find_element_by_css_selector("#su").click()


time.sleep(8)
driver.quit()
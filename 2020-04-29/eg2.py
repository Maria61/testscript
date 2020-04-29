from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com")

# 练习操作相应的元素

# driver.find_element_by_id("kw").send_keys("Ella")
# driver.find_element_by_id("su").click()
# time.sleep(6)
# # 练习clear清除对象的内容
# driver.find_element_by_id("kw").clear()
# driver.find_element_by_id("kw").send_keys("蔡徐坤")
# # 练习submit提交按钮
# driver.find_element_by_id("su").submit()
# time.sleep(6)
# 练习获取元素的文本内容
text = driver.find_element_by_id("s-bottom-layer-right").text
print(text)

driver.quit()
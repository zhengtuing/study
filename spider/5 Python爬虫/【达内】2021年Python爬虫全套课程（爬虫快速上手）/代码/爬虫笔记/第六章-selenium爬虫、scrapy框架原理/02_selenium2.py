"""
1、打开浏览器,输入百度的URL地址
2、输入搜索关键字:赵丽颖
3、找到百度一下按钮,进行点击
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

# 找到搜索框节点,并发送搜索关键字
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
driver.find_element_by_xpath('//*[@id="su"]').click()





















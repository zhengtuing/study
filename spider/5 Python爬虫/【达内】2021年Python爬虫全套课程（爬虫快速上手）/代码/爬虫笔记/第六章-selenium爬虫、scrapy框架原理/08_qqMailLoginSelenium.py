"""
使用selenium模拟登录qq邮箱
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='https://mail.qq.com/')

# 1、切换iframe子页面
driver.switch_to.frame('login_frame')

# 2、用户名、密码、登录
driver.find_element_by_id('u').send_keys('2621470058')
driver.find_element_by_id('p').send_keys('zhanshen001')
driver.find_element_by_id('login_button').click()
















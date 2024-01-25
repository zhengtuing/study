"""
使用selenium模拟登录豆瓣网
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(url='https://www.douban.com/')

# 1、切换到iframe子页面
iframe_node = driver.find_element_by_xpath('//*[@id="anony-reg-new"]/div/div[1]/iframe')
driver.switch_to.frame(iframe_node)

# 2、找到密码登录,并点击
driver.find_element_by_xpath('/html/body/div[1]/div[1]/ul[1]/li[2]').click()

# 3、用户名、密码、登录豆瓣
driver.find_element_by_id('username').send_keys('15110225726')
driver.find_element_by_id('password').send_keys('zhanshen001')
driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div[5]/a').click()

















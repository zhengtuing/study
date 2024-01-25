# 需要导入selenium的webdriver接口
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

# 1、save_screenshot() : 获取屏幕截图
driver.save_screenshot('baidu.png')
# 2、maximize_window() : 浏览器窗口最大化
driver.maximize_window()
# 3、quit() : 关闭浏览器
# driver.quit()
# 4、page_source : HTML结构源码
html = driver.page_source
# 5、find() : 在html结构源码中查找某个字符串是否存在,记住: 查找失败,返回-1
#             经常用来判断是否为最后一页
print(driver.page_source.find('aaaaaaaaaaaaaaaaaaaaaa'))










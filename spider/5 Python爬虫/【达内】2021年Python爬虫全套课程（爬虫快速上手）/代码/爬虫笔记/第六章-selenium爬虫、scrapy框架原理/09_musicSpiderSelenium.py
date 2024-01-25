"""
抓取网易云音乐排行榜
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url='https://music.163.com/#/discover/toplist')

# 1、切换iframe子页面
driver.switch_to.frame('contentFrame')

# 2、提取具体歌曲信息
tr_list = driver.find_elements_by_xpath('//table/tbody/tr')
for tr in tr_list:
    item = {}
    item['rank'] = tr.find_element_by_xpath('.//span[@class="num"]').text.strip()
    item['name'] = tr.find_element_by_xpath('.//span[@class="txt"]/a/b').get_attribute('title').strip().replace('\xa0', ' ')
    item['time'] = tr.find_element_by_xpath('.//span[@class="u-dur "]').text.strip()
    item['star'] = tr.find_element_by_xpath('.//div[@class="text"]/span').get_attribute('title').strip()

    print(item)

# 数据抓取完成后关闭浏览器
driver.quit()
















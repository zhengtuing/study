"""
使用selenium抓取猫眼电影top100
"""
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

driver.get(url='https://maoyan.com/board/4')

def get_one_page():
    """获取一页的数据的函数"""
    # 基准xpath: 匹配每个电影信息的dd节点对象列表
    dd_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for dd in dd_list:
        # text属性 : 获取当前dd节点以及它的子节点和后代节点的文本内容
        one_film_info_list = dd.text.split('\n')
        item = {}
        item['rank'] = one_film_info_list[0].strip()
        item['name'] = one_film_info_list[1].strip()
        item['star'] = one_film_info_list[2].strip()
        item['time'] = one_film_info_list[3].strip()
        item['score'] = one_film_info_list[4].strip()
        print(item)

while True:
    get_one_page()
    try:
        # selenium找节点时,如果找不到,会抛出异常
        driver.find_element_by_link_text('下一页').click()
    except Exception as e:
        # 一旦捕获到异常,说明已经是最后一页
        driver.quit()
        break









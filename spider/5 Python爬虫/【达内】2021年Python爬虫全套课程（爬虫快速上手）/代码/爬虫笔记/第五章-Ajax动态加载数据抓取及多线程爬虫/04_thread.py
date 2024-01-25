"""
多线程回顾
"""
from threading import Thread

def spider():
    print('也许时间是一种解药')

t_list = []
for i in range(5):
    t = Thread(target=spider)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()
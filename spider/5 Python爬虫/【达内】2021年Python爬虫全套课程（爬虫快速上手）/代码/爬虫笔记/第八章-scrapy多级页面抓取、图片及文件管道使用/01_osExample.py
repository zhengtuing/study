"""
创建目录结构：./novel/盗墓笔记1:七星鲁王宫/
保存文件：    ./novel/盗墓笔记1:七星鲁王宫/七星鲁王_第一章_血尸.txt
"""
import os

parent_title = '盗墓笔记1七星鲁王宫'
son_title = '七星鲁王 第一章 血尸'

directory = './novel/{}/'.format(parent_title)
if not os.path.exists(directory):
    os.makedirs(directory)

# ./novel/盗墓笔记1:七星鲁王宫/七星鲁王_第一章_血尸.txt
filename = '{}{}.txt'.format(directory, son_title.replace(' ', '_'))
with open(filename, 'w') as f:
    f.write('我是小说内容')













"""
正则表达式分组示例
"""

import re

html = 'A B C D'
pattern = re.compile('\w+\s+\w+')
r_list = pattern.findall(html)
# r_list: ['A B','C D']

pattern = re.compile('(\w+)\s+\w+')
r_list = pattern.findall(html)
# 第1步：['A B','C D']
# 第2步：['A','C']
print(r_list)

pattern = re.compile('(\w+)\s+(\w+)')
r_list = pattern.findall(html)
# 第1步：['A B','C D']
# 第2步：[('A','B'),('C','D')]
print(r_list)






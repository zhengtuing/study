"""
csv模块示例
"""
import csv

# writerow([])：单行写入
with open('teachers.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['超哥哥','spider'])

# writerows([(),(),(),()])：多行写入 - 一次性写入多行数据
teachers_li = [
    ('步惊云','排云掌'),
    ('聂风','风神腿'),
    ('雄霸','三分归元气')
]
with open('teachers.csv','a',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(teachers_li)








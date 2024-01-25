"""
json模块中dump()方法的使用
"""
import json

app_list = [
    {'name':'腾讯QQ' , 'link':'http://qq.com/', 'type':'聊天社交'},
    {'name':'王者荣耀', 'link':'http://game.com/', 'type':'游戏'},
    {'name':'真三国无双', 'link':'http://country.com/', 'type':'魔兽争霸与冰封王座'}
]

with open('app.json', 'w', encoding='utf-8') as f:
    json.dump(app_list, f, ensure_ascii=False)









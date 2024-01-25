# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

class DaomuPipeline(object):
    def process_item(self, item, spider):
        # filename: ./novel/{}/{}.txt
        filename = './novel/{}/{}.txt'.format(
            item['parent_title'].replace(':', '_'),
            item['son_title'].replace(' ', '_')
        )
        with open(filename, 'w') as f:
            f.write(item['novel_content'])

        return item












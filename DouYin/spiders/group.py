# -*- coding: utf-8 -*-
import json
import re
import time
from copy import deepcopy

import pymysql
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
import requests

upload_url = 'http://49.232.202.165:8000/groupr/'


class GroupSpider(RedisCrawlSpider):
    name = 'group'

    def make_request_from_data(self, data):
        item = {}
        data = json.loads(data)
        url = data['url']
        ts = data['ts']
        gorgon = data['gorgon']
        group_id = data['group_id']
        item['group_id'] = group_id

        return scrapy.Request(url, headers={
            'authority': ':	api3-normal-c-lf.amemv.com',
            'x-tt-token': '00091549e1c9c85687b190363f7a97c66294103deea64cae92be63ed893da1856df385f3066575f4e3029f1cb1405818b9f ',
            'sdk-version': '1 ',
            'user-agent': 'Aweme 10.3.0 rv:103020 (iPhone; iOS 13.6; zh_CN) Cronet ',
            'x-ss-dp': '1128 ',
            'x-tt-trace-id': '00-0089231609872286b83408a916e10468-0089231609872286-01 ',
            'accept-encoding': 'gzip, deflate, br ',
            'x-khronos': ts,
            'x-gorgon': gorgon,
        }, callback=self.parse, dont_filter=True, meta={'item': deepcopy(item)})

    def parse(self, response):
        item = response.meta['item']
        group_id = item['group_id']
        try:
            datas = json.loads(response.text)
            group_name = datas['data']['share_data'][2]['description'].replace('\n', '')
            re_data = re.search(r'在抖音创建了群聊“(.*)”，?', group_name).group(1)

            if len(re_data) > 0:
                print('不是空群')

                data = {
                    'req_data': group_id
                }
                req = requests.post(upload_url, data=data)

            elif len(re_data) == 0:
                print('是空群')
                # print(qr_text)
                print('------------------')

        except Exception as f:
            print(f)

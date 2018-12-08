# -*- coding: utf-8 -*-
"""
Created on Sat Dec  1 10:41:51 2018

@author: Lenovo
"""

import requests
import time
import re
import json

def get_one_page(url):
    headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2263.400 QQBrowser/9.5.10429.400',
            'Referer':'https://movie.douban.com/chart',
            'Host':'movie.douban.com'
            }
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        return None
#<li>.*?pic.*?em.*?>(.*?)</em>.*?src="(.*?)"</a>.*?info.*?hd.*?a.*?span.*?title.*?>(.*?)</span>.*?bd.*?p>(.*?)<br>(.*?)</p>.*?star.*?rating_num>(.*?)</span>.*?</li>
def parse_one_page(html):
    pattern=re.compile('<em class="">(\d+)</em>.*?<span class="title">(.*?)</span>.*?<p class="">(.*?)</p>.*?<span class="rating_num" property="v:average">(.*?)</span>.*?<span>(.*?)</span>.*?<span class="inq">(.*?)</span>',re.S)
    items=re.findall(pattern,html)
    for item in items:
        yield{
                '排名':item[0],
                'img':item[1],
                '电影名':item[2],
                '职员表':item[3],
                '上映时间':item[4],
                '分数':item[5]
                }
        with open('douban1201.txt','a',encoding='utf-8') as f:
            f.write(json.dumps(dict,ensure_ascii=False)+'\n')

#https://movie.douban.com/top250?start=75
def main(offset):
    url='https://movie.douban.com/top250?start='+str(offset)+'&filter='
    html=get_one_page(url)
    parse_one_page(html)
    
for i in range(10):
    main(offset=i*25)
    time.sleep(1)
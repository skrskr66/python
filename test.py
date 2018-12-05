# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 11:58:36 2018

@author: Lenovo
"""

import json
import requests
import time
from bs4 import BeautifulSoup
import re
def get_one_page(url):
    headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2263.400 QQBrowser/9.5.10429.400'}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    else:
        return None
data=[]
def parse_one_page(html):
#    soup=BeautifulSoup(''.join(html),'lxml')
##在这里我们是得到了R.txt的文本，但是我们不能输出，所以我们得利用print来输出
#    titles=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.name > a')
#    pics=soup.select('#app > div > div > div.main > dl > dd > a > img.board-img')
#    actors=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.star')
#    days=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-info > p.releasetime')
#    scores1=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-number.score-num > p > i.integer')
#    scores2=soup.select('#app > div > div > div.main > dl > dd > div > div > div.movie-item-number.score-num > p > i.fraction')
#    for title,pic,actor,day,scores,scoress in zip(titles,pics,actors,days,scores1,scores2):
#        info={
#                'title':title.get_text(),
#                'pic':pic.get('alt'),
#                'actor':actor.get_text(),
#                'day':day.get_text(),
#                'scores':scores.get_text()+scoress.get_text(),
#                }
#        write_to_file(info)
#        #data.append(info)
#        print(info)
    pattern=re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items=re.findall(pattern,html)
    for item in items:         
        yield{             
                'index':item[0],
                'img':item[1],
                '名称':item[2],
                '主演':item[3].strip()[3:],
                '上映时间':item[4].strip()[5:]
                }
def write_to_file(content):
    with open('maoyan.excel','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url='https://maoyan.com/board/4?offset='+str(offset)
    html=get_one_page(url)
    parse_one_page(html)
'''
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)
''' 
for i in range(10):
    main(offset=i*10)
    time.sleep(1)

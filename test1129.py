# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 13:20:18 2018

@author: Lenovo
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
urls=['https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start={}&limit=20'.format(number*20) for number in range(0,5)]
headers={
        'Host': 'movie.douban.com',
        'Referer': 'https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        }
def get_url(url):
#    params={
#            'type':'5',
#            'interval_id':'100%3A90',
#            'limit':'20',
#            'start':start
#            }
    try:
        response=requests.get(url,headers=headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
            print('Error',e.args)
            
def parse_page(json):
    if json:
        for index,item in enumerate(json):
            douban={}
            douban['title']=item['title']
            douban['rank']=item['rank']
            douban['type']=item['types']
            douban['actors']=item['actors']
            douban['score']=item['score']
            yield douban
            
def write_to_file(content):
    content2=pd.DataFrame(content)
    content2.to_csv('douban.csv',encoding='utf_8_sig',mode='a')
films=[] 
for url in urls:
    json=get_url(url)
    results=parse_page(json)
    time.sleep(1)
    for result in results:
        print(result)
        films.append(result)
write_to_file(films)
#maxpage=100
#for start in range(0,maxpage+1):
#    json=get_url(start)
#    results=parse_page(json)
#    for result in results:
#        print(result)
#        time.sleep(2)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
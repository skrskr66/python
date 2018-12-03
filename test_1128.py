# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:10:22 2018

@author: Lenovo
"""
import requests
from bs4 import BeautifulSoup
import time
import json

urls=['https://xa.58.com/tech/pn{}/'.format(number) for number in range(1,10)]
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2263.400 QQBrowser/9.5.10429.400','Referer':'https://pos.baidu.com/wh/o.htm?ltr='}
#print(urls)
#def get_url(url):
#    r=requests.get(url,headers=headers)
#    soup=BeautifulSoup(r.text,'lxml')
#    links=soup.select('#page_list > ul > li > a')
#    for link in links:
#        href=link.get("href")
#        print(href)
#
#for url in urls:
#    get_url(url)
#    time.sleep(2)
#headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2263.400 QQBrowser/9.5.10429.400','Referer':'https://pos.baidu.com/wh/o.htm?ltr='}
def get_url(url):
    wb_data=requests.get(url,headers=headers)
    wb_data.raise_for_status
    wb_data.encoding=wb_data.apparent_encoding
    soup=BeautifulSoup(wb_data.text.strip(),'lxml')
    links=soup.select("#list_con > li > div.item_con.job_title > div.job_name.clearfix > a")
    for link in links:
        href=link.get("href")
        get_info(href)

def get_info(url):
    wb_data=requests.get(url,headers=headers)
    soup=BeautifulSoup(wb_data.text.strip(),'lxml')
    companys=soup.select("body > div.con > div.rightCon > div:nth-of-type(1) > div > div.comp_baseInfo_title > div.baseInfo_link")
    posts1=soup.select("body > div.con > div.leftCon > div.item_con.pos_info > div.pos_base_info > span.pos_title")
    posts2=soup.select("body > div.con > div.leftCon > div.item_con.pos_info > span")
    locates=soup.select("body > div.con > div.leftCon > div.item_con.pos_info > div.pos-area > span:nth-of-type(2)")
    moneys=soup.select("body > div.con > div.leftCon > div.item_con.pos_info > div.pos_base_info > span.pos_salary")
    welfares=soup.select("body > div.con > div.leftCon > div.item_con.pos_info > div.pos_welfare")
#    requires=soup.select("body > div.con > div.leftCon > div.item_con.pos-intro > div.subitem_con.pos_description > div.posDes > div.des")
    for company,post1,post2,money,locate,welfare in zip(companys,posts1,posts2,moneys,locates,welfares):
        data={  
                "company":company.get_text(),
                "post":post1.get_text()+post2.get_text(),
                "money":money.get_text(),
                "locate":locate.get_text(),
                "welfare":welfare.get_text(),
#                "require":require.get_text(),
                }
        write_to_file(data)
        print(data)


def write_to_file(content):
    with open('58同城.text','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')



for url in urls:
    get_url(url)
    time.sleep(2)











#for url in urls:
#    get_url(url)
#    time.sleep(5)


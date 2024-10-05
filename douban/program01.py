#coding=utf-8

import code
from bs4 import BeautifulSoup   #网页解析，获取数据
import re     
import urllib.request,urllib.error #指定URL，获取网页数据
import xlwt   #进行excel处理
import sqlite3#进行SQLite 数据库操作

def main():
    base_url='https://movie.douban.com/top250?start='
#1.爬取网页
    datalist=getData(base_url)
#2.解析数据(一个一个的解析)
    for i in range(10):
        url=base_url+str(i*25)
        html=askURL(url)
#3，保存数据
    save_path='.\\豆瓣电影Top250.xls'
    saveData(save_path)




#1.爬取网页
def getData(base_url):
    datalist=[]
    #2.解析数据(一个一个的解析)

    return datalist






#得到一个指定的URL
def askURL(url):
    head={#模拟浏览器头部信息，向豆瓣服务器发信息
        #伪装成浏览器
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    }
    request=urllib.request.Request(url=url,headers=head)
    html=''#存储

    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e,code)
        # if hasattr(e,"reason"):
        #     print(e,reason) 
        
    return html
     
 


#3，保存数据
def saveData(save_path):
    pass







# if __name__=='__main__':
#     main()
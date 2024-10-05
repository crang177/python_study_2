import  requests,re,os
from bs4 import BeautifulSoup
from selenium import webdriver


# browser=webdriver.Edge()
# browser.get("https://www5.baidu.com/")
# print(type(browser))


#https://webfs.kugou.com/202410050053/d6b6083f91b146dad1805ceb879ddc29/v3/04a21db1ab3c8e0d1d8f51f11bdb03a1/yp/full/ap1014_us0_mii0w1iw8z2ai2iphcu80ooo2ki81120_pi406_mx595775928_s3256085660.mp3
url="https://www.kugou.com/song/rank.htm?rank=31310#9upjnc1d"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "Referer":"https://www.kugou.com/",
    "cookie":"kg_mid=e8028051482f72b07c7cf6d3fc7471b2; kg_dfid=2mRXP213DpsQ3rEE910QHgbi; KuGooRandom=66141727971294693; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; kg_mid_temp=e8028051482f72b07c7cf6d3fc7471b2; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; KuGoo=KugooID=598927035&KugooPwd=5E9C4A23CA9DB05E86A3A2B45C38A614&NickName=%u0020%u706d%u5929%u2192%u795e%u8bdd&Pic=http://imge.kugou.com/kugouicon/165/20240813/20240813010544832930.jpg&RegState=1&RegFrom=&t=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c&a_id=1014&ct=1728061153&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0035%u0039%u0038%u0039%u0032%u0037%u0030%u0033%u0035&t1=; KugooID=598927035; t=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c; a_id=1014; UserName=kgopen598927035; mid=e8028051482f72b07c7cf6d3fc7471b2; dfid=2mRXP213DpsQ3rEE910QHgbi",
}


os.system("cls")
response=requests.get(url=url,headers=headers)
response.encoding=response.apparent_encoding
response.raise_for_status()
print(response.text)
soup=BeautifulSoup(response.text,'html.parser')
print(soup)

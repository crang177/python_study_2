# import requests

# res=requests.get("https://www.baidu.com")
# if res.status_code==requests.codes.ok:
#     file=open('baidu.txt','wb')
#     for chunk in res.iter_content(100000):
#         file.write(chunk)
#     file.close()


import urllib.parse
import urllib.request,urllib.error
import os
os.system("cls")

url="https://www.baidu.com"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",

}

res= urllib.request.Request(url=url,headers=headers)
response=urllib.request.urlopen(res)
print(response.read().decode("utf-8"))
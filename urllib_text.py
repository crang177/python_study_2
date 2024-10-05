import urllib.parse
import urllib.request,urllib.error
import os
os.system("cls")

url="https://httpbin.org//post"
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",

}
data=bytes(urllib.parse.urlencode({"a":"f"}),encoding='utf-8')
res= urllib.request.Request(url=url,data=data,headers=headers)
response=urllib.request.urlopen(res)
print(response.read().decode("utf-8"))
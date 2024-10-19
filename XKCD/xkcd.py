import requests,re,os
from bs4 import BeautifulSoup
import pyinputplus as pyip



os.system("cls")



n=pyip.inputInt(prompt="请输入要下载漫画的页数： ")
for i in range(n):
    url=f"https://xkcd.com/{i+1}/"
    headers={
        "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Mobile Safari/537.36 Edg/130.0.0.0",
        "Referer":"https://xkcd.com/1/",
    }

    res=requests.get(url=url,headers=headers)
    res.encoding=res.apparent_encoding
    res.raise_for_status()

    bs=BeautifulSoup(res.text,"html.parser")

    cartoonRegexes=re.compile(r'<.*c="(.*)".*title')
    cartoon_url_list=cartoonRegexes.findall(res.text)
    for i in cartoon_url_list:
        cartoon_url=i
        for j in list(bs.find_all("img")) :
            if cartoon_url in str(j):
                
                NameRegexes=re.compile(r'title="(.*)"')
                name_list=NameRegexes.findall(str(j))
                for k in name_list:
                    cartoon_name=k
                break

    download_url=url+cartoon_url

    # 替换不合法字符
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', cartoon_name)
    # 处理其他可能的非法字符，例如《和》
    safe_name = re.sub(r'[《》.]', '', safe_name)

    with open(f"XKCD\\{safe_name}.jpg","wb") as fp :
        response=requests.get(download_url)
        fp.write(response.content)
        print(f"漫画 {safe_name} 下载成功")








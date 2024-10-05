import requests
import re,os
import pyinputplus as pyip

#爬取彼岸图网站上的图片（较高的分辨率）：按照首页的页数爬取


os.system("cls")
n=pyip.inputInt(prompt="请输入第多少页：")
url_1=f"https://pic.netbian.com/index_{n}.html"#要爬的网站页数
url="https://pic.netbian.com"#用来当下载时前部分的地址
headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
}


href=re.compile(r'<a href="(/tu.*?)"[0-9a-zA-Z.]? target=".*?">')#这个正则表达式用于在url_1中去找到原图的网站地址
# parr=re.compile(r'src="(/u.*?)".alt="(.*?)"')
parr=re.compile(r'src="(/u.*?)".data.*alt="(.*?)"')#找到src即下载的地址（只有后部分，要与url连接）


if n==1:
    url_1="https://pic.netbian.com/"
    href=re.compile(r'<a href="(/tu.*?)".title=".*?"')
response=requests.get(url=url_1,headers=headers)
response.encoding=response.apparent_encoding#防止乱码
response.raise_for_status()


pic_href=href.findall(response.text)#得到网站中当前页面的所有原图的地址
for i in pic_href:
    res1=requests.get(url+i)#爬取到原图的地址，得到其源代码
    res1.encoding=response.apparent_encoding
    image=parr.findall(res1.text)
    link,name=image[0]#得到一个元组列表，元组第一项为下载当前原图片的地址的后半部分

    # 替换不合法字符
    safe_name = re.sub(r'[<>:"/\\|?*]', '_', name)
    # 处理其他可能的非法字符，例如《和》
    safe_name = re.sub(r'[《》]', '', safe_name)

    with open(f'picture\\{safe_name}.jpg','wb') as img:
        res2=requests.get(url+link)#url+link得到完整下载地址，爬取得到原图下载地址网站的所有信息
        img.write(res2.content)#下载原图，content为Response的一个属性（处理原始数据，不会对数据进行解码），通常用于二进制数据，比如音频，图片，非文本格式数据
        img.close()
    print(f'图片  "{name}"  下载成功\n')













# image=parr.findall(response.text)

# for i in image:
#     link=i[0]
#     name=i[1]
    
    
#     with open(f"picture\\{name}.jpg","wb") as img:
#         res=requests.get("https://pic.netbian.com"+link)
#         img.write(res.content)
#         img.close()
#     print(f"照片{name}下载成功\n")









 
# import matplotlib.pyplot as plt
# from PIL import Image
 
 
# def produceImage(file_in, width, height, file_out):
#     image = Image.open(file_in)
#     resized_image = image.resize((width, height),)
#     resized_image.save(file_out)
 
 
# if __name__ == '__main__':
#     file_in = 'picture\\1.jpg'
#     width = 3840 #调整的分辨率大小
#     height = 2160
#     file_out = 'picture\\2.jpg'
#     # 分辨率
#     produceImage(file_in, width, height, file_out)

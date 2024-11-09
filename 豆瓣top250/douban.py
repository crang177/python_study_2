import requests
from lxml import etree
import csv

url="https://movie.douban.com/top250"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "Cookie":'bid=oO7SRcSCols; douban-fav-remind=1; _pk_id.100001.4cf6=7e1fa86abd58d7af.1727852752.; __yadk_uid=mlRRZe3NFdDEz3IkMIYT2O1sZMGuM2vB; ll="118254"; dbcl2="284652672:c24MVYPCJE8"; ck=4a2Q; _ga=GA1.1.1106876284.1731131112; _ck_desktop_mode=1; vmode=pc; push_noty_num=0; push_doumail_num=0; _ga_Y4GN1R87RG=GS1.1.1731131111.1.1.1731131145.0.0.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1731131173%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1bid=oO7SRcSCols; douban-fav-remind=1; _pk_id.100001.4cf6=7e1fa86abd58d7af.1727852752.; __yadk_uid=mlRRZe3NFdDEz3IkMIYT2O1sZMGuM2vB; ll="118254"; dbcl2="284652672:c24MVYPCJE8"; ck=4a2Q; _ga=GA1.1.1106876284.1731131112; _ck_desktop_mode=1; vmode=pc; push_noty_num=0; push_doumail_num=0; _ga_Y4GN1R87RG=GS1.1.1731131111.1.1.1731131145.0.0.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1731131173%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=1'
}
response=requests.get(url =url,headers=headers)
response.encoding=response.apparent_encoding
selector=etree.HTML(response.text)
ls=selector.xpath('//div[@class="info"]')
for i in ls:
    href=i.xpath("./div/a/@href")[0]
    text=i.xpath("./div/a/span[1]/text()")[0].strip()
    star=i.xpath('./div/div[@class="star"]/span[2]/text()')[0].strip()
    dictionary=[{
        "电影":text,
        "评分":star,
        "网址":href,
    }]
    with open ("豆瓣top250/movie.csv","a",encoding="utf=8") as fp:
        fp=csv.writer(fp)
        fp.writerow(dictionary)

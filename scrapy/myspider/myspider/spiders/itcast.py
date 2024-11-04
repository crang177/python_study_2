import scrapy


class ItcastSpider(scrapy.Spider):
    name = "itcast"
    allowed_domains = ["itcast.cn"]
    start_urls = ["https://www.itheima.com/teacher.html#ajavaee?cz-pc-dh}"]

    def parse(self, response):
        # with open("itcast.html","wb") as f:
        #     f.write(response.body)
        #获取的是所有教师的节点
        t_list=response.xpath('//div[@class="li_txt"]')

        teacher_list=[]
        #遍历教师列表的节点，利用节点的xpath对数据进行提取
        for t in t_list:
            temp={}
            temp["name"]=t.xpath('./h3/text()')
            temp["position"]=t.xpath('./h4/text()')
            temp["information"]=t.xpath('./p/text()')
            teacher_list.append(temp)
            print(temp)
        

        


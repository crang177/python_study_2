import shutil,os

ls=os.listdir('E:\BaiduNetdiskDownload\爬虫开发+APP逆向超级大神班\爬虫7期 爬虫逆7期\第七模块：APP逆向\spider1')

for i in ls :
    #shutil.move('E://BaiduNetdiskDownload//爬虫开发+APP逆向超级大神班//爬虫7期 爬虫逆7期\第七模块：APP逆向\spider1//'+i ,'E://BaiduNetdiskDownload//爬虫开发+APP逆向超级大神班//爬虫7期 爬虫逆7期\第七模块：APP逆向\spider1//'+i[25:] )
    
    name=i[:-22]+".mp4"
    shutil.move('E://BaiduNetdiskDownload//爬虫开发+APP逆向超级大神班//爬虫7期 爬虫逆7期\第七模块：APP逆向\spider1//'+i ,'E://BaiduNetdiskDownload//爬虫开发+APP逆向超级大神班//爬虫7期 爬虫逆7期\第七模块：APP逆向\spider1//'+name)

  
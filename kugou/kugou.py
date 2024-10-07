import  requests,re,os
import hashlib
import time
from  bs4 import BeautifulSoup
import pyinputplus as pyip

os.system("cls")
#获取单首歌曲
def Onesong():
    url="https://wwwapi.kugou.com/play/songinfo"
    data={#查询参数
        "srcappid": "2919",
        "clientver": "20000",
        "clienttime": "1728109820904",
        "mid": "e8028051482f72b07c7cf6d3fc7471b2",
        "uuid": "e8028051482f72b07c7cf6d3fc7471b2",
        "dfid": "2mRXP213DpsQ3rEE910QHgbi",
        "appid": "1014",
        "platid": "4",
        "encode_album_audio_id": "9upjnc1d",
        "token": "eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c",
        "userid": "598927035",
        "signature": "638e07e0b03c40b8ae27fed29a03a29e",
    }
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        "Referer":"https://www.kugou.com/",
        "cookie":"kg_mid=e8028051482f72b07c7cf6d3fc7471b2; kg_dfid=2mRXP213DpsQ3rEE910QHgbi; KuGooRandom=66141727971294693; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; kg_mid_temp=e8028051482f72b07c7cf6d3fc7471b2; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; KuGoo=KugooID=598927035&KugooPwd=5E9C4A23CA9DB05E86A3A2B45C38A614&NickName=%u0020%u706d%u5929%u2192%u795e%u8bdd&Pic=http://imge.kugou.com/kugouicon/165/20240813/20240813010544832930.jpg&RegState=1&RegFrom=&t=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c&a_id=1014&ct=1728061153&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0035%u0039%u0038%u0039%u0032%u0037%u0030%u0033%u0035&t1=; KugooID=598927035; t=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c; a_id=1014; UserName=kgopen598927035; mid=e8028051482f72b07c7cf6d3fc7471b2; dfid=2mRXP213DpsQ3rEE910QHgbi",
    }

    response=requests.get(url=url,params=data,headers=headers)  #params为查询参数
    response.encoding=response.apparent_encoding
    json_data=response.json()#得到json文件格式
    play_url=json_data["data"]["play_url"]#找到下载音乐的url
    name=json_data["data"]["audio_name"]#歌曲的名字

    with open(f"kugou\\{name}.mp3","wb") as  music:
        res=requests.get(play_url)#得到下载歌曲界面的源码
        music.write(res.content)#下载歌曲
    print(name)


#对加密参数signature进行构建加秘处理
def signature_md5(data_time,music_id):
    s=['NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt', 
       'appid=1014', 
       f"clienttime={data_time}", 
       'clientver=20000', 
       'dfid=2mRXP213DpsQ3rEE910QHgbi', 
       f"encode_album_audio_id={music_id}", 
       'mid=e8028051482f72b07c7cf6d3fc7471b2', 
       'platid=4',
       'srcappid=2919', 
       'token=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c', 
       'userid=598927035',
       'uuid=e8028051482f72b07c7cf6d3fc7471b2',
       'NVPh5oo715z5DIWAeQlhMDsWXXQV4hwt']
    string="".join(s)
    MD5=hashlib.md5()
    MD5.update(string.encode("utf-8"))
    signature=MD5.hexdigest()
    return signature
#对酷狗音乐的一个榜单爬取音乐
def list_music():
    url=pyip.inputStr(prompt="输入榜单的链接：",allowRegexes=r'https:://.*')
    #url="https://www.kugou.com/yy/rank/home/1-49225.html?from=rank"
    url1="https://wwwapi.kugou.com/play/songinfo"

    headers={

            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
            "Referer":"https://www.kugou.com/",
            "cookie":"kg_mid=e8028051482f72b07c7cf6d3fc7471b2; kg_dfid=2mRXP213DpsQ3rEE910QHgbi; KuGooRandom=66141727971294693; kg_dfid_collect=d41d8cd98f00b204e9800998ecf8427e; ACK_SERVER_10015=%7B%22list%22%3A%5B%5B%22bjlogin-user.kugou.com%22%5D%5D%7D; kg_mid_temp=e8028051482f72b07c7cf6d3fc7471b2; ACK_SERVER_10016=%7B%22list%22%3A%5B%5B%22bjreg-user.kugou.com%22%5D%5D%7D; ACK_SERVER_10017=%7B%22list%22%3A%5B%5B%22bjverifycode.service.kugou.com%22%5D%5D%7D; KuGoo=KugooID=598927035&KugooPwd=5E9C4A23CA9DB05E86A3A2B45C38A614&NickName=%u0020%u706d%u5929%u2192%u795e%u8bdd&Pic=http://imge.kugou.com/kugouicon/165/20240813/20240813010544832930.jpg&RegState=1&RegFrom=&t=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c&a_id=1014&ct=1728061153&UserName=%u006b%u0067%u006f%u0070%u0065%u006e%u0035%u0039%u0038%u0039%u0032%u0037%u0030%u0033%u0035&t1=; KugooID=598927035; t=eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c; a_id=1014; UserName=kgopen598927035; mid=e8028051482f72b07c7cf6d3fc7471b2; dfid=2mRXP213DpsQ3rEE910QHgbi",
        }

    response=requests.get(url=url,headers=headers)            
    response.encoding=response.apparent_encoding
    response.raise_for_status()

    eid_nameRe=re.compile(r'<.*title="(.*)" data.*data-eid="(.*)">')
    t_list=eid_nameRe.findall(response.text)

    for i in t_list:
        i=list(i)
        name,eid=i
        music_id=eid
        data_time=int(time.time()*1000)
        signature=signature_md5(data_time=str(data_time),music_id=music_id)
        data={#查询参数
            "srcappid": "2919",
            "clientver": "20000",
            "clienttime":str(data_time),
            "mid": "e8028051482f72b07c7cf6d3fc7471b2",
            "uuid": "e8028051482f72b07c7cf6d3fc7471b2",
            "dfid": "2mRXP213DpsQ3rEE910QHgbi",
            "appid": "1014",
            "platid": "4",
            "encode_album_audio_id": music_id,
            "token": "eee2408a1a728772422bde818ea19ef3c768d0bc5568eab32bd0579e497d336c",
            "userid": "598927035",
            "signature": signature,
        }
        
        res1=requests.get(url=url1,params=data,headers=headers) 
        res1.encoding=res1.apparent_encoding
        res1.raise_for_status()

        json_data=res1.json()

        play_url=json_data['data']['play_url']

        # 替换不合法字符
        safe_name = re.sub(r'[<>:"/\\|?*]', '_', name)
        # 处理其他可能的非法字符，例如《和》
        safe_name = re.sub(r'[《》]', '', safe_name)
        with open(f"kugou\\{safe_name}.mp3","wb") as music:
            res2=requests.get(play_url)
            music.write(res2.content)

        print(f"歌曲 “{name}” 下载完毕")
#对比了查询参数data，找到了每个音乐之间的三个区别（剩余9个都相同）：
#    clienttime：时间戳，可以用time.time（）得到
#    enencode_album_audio_id：音频id，就是播放音乐界面中的网址的最后面一部分，可以直接在浏览器抓包得到
#    signature：签名认证，加密参数，（抓包分析时直接搜索signature，打开所得结果，进行断点刷新调试，找到与data相似部分，然后构建一个类似作用的函数来解密得到）
              #要用到哈希模块（hashlib）：加密过程：
                                        # MD5=hashlib.md5()
                                        # MD5.update(string.encode("utf-8"))
                                        # signature=MD5.hexdigest()


list_music()















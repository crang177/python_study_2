#!python3
import webbrowser
import sys,pyperclip

#cd D:\GithubData\python_study_2
#中国湖北省武汉市
#https://www.google.com.hk/maps/place/%E4%B8%AD%E5%9B%BD%E6%B9%96%E5%8C%97%E7%9C%81%E6%AD%A6%E6%B1%89%E5%B8%82/@30.5680122,114.1355772,11z/data=!3m1!4b1!4m6!3m5!1s0x342eaef8dd85f26f:0x39c2c9ac6c582210!8m2!3d30.5927599!4d114.30525!16zL20vMGwzY3k?hl=zh-CN&entry=ttu&g_ep=EgoyMDI0MDkyNS4wIKXMDSoASAFQAw%3D%3D

#https://hunanapp.weather.com.cn/city/citysearch.shtml?fromurl=mweather15d&areaid=index



if len(sys.argv)>1:
    address=' '.join(sys.argv[1:])
else:
    address=pyperclip.paste()

#webbrowser.open('https://www.google.com.hk/maps/place/'+address)

webbrowser.open("https://www.weather.com.cn/weather15d/101200101.shtml")
webbrowser.open("https://ai.yiios.com/#/chat")
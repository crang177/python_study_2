from selenium import webdriver 
from selenium.webdriver.common.by import By
import time,os


os.system("cls")
#不直接退出浏览器的方法
# option=webdriver.EdgeOptions()
# option.add_experimental_option("detach",True)
# browser=webdriver.Edge(options=option)
browser=webdriver.Edge()#直接退出浏览器
browser.get("http://172.30.21.100/tpl/whut/login.html?acip=172.30.1.223&acname=WHUT-Bras-ME60-A&ip=10.84.131.112&nasId=52&userip=10.84.131.112&wlanacname=")

#根据标签By.ID（找到<input>中去了）去查找ID的值value（即元素)，返回一个WebElement对象，这个对象有一个click（）方法，模拟鼠标在该元素上单击
#ID具有唯一性
user_name=browser.find_element(by=By.ID,value="username")
password=browser.find_element(by=By.ID,value="password")
btn=browser.find_element(By.ID,"login-account")

#给Web页面的文本字段发送按键事件信息。找到那个文本字段的<input>元素，send_keys("")方法为输入的按键消息
user_name.send_keys("357128")
password.send_keys("ran1856.")

#模拟单击（webelement方法）
btn.click()

time.sleep(2)
browser.close()

from selenium import webdriver
import os,time,sys,re  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

os.system("cls")
handles=[]#保存每次跳转页面的句柄
url="https://mail.whut.edu.cn/"
option=webdriver.EdgeOptions()
option.add_experimental_option("detach",True)
browser=webdriver.Edge(options=option)

browser.get(url=url)
handles.append(browser.window_handles[0])

id=browser.find_element(By.ID,"account_name") 
password=browser.find_element(By.ID,value="password")
btn=browser.find_element(By.ID,value="action")
id.send_keys("357128")
password.send_keys("密码")
btn.click()

#browser.window_handles[0]Webdriver的属性window_handles用来记录当前页面的句柄，当前页面的句柄为列表的第一项，所以为0
#browser.switch_to.window为Webdriver的方法switch_to.window（）移动句柄到某一个新页面
#此时的browser就到了新页面的Webdriver对象
browser.switch_to.window(browser.window_handles[0])
handles.append(browser.window_handles[0])
#Webdriver对象的current_url（）方法，用来获取此时的url，由于f‘’中是表达式，所以方法的（）不表示出来
#print(f'{browser.current_url}')
write_email_btn=browser.find_element(By.ID,"_mail_component_41_41")
write_email_btn.click()

browser.switch_to.window(browser.window_handles[0])
handles.append(browser.window_handles[0])
receive_address=browser.find_element(By.CLASS_NAME,"nui-editableAddr-ipt")








# # if len(sys.argv)>1:
# #     receive_address.send_keys(sys.argv[1])
# #     content="".join(sys.argv[2:])
# # send_content.send_keys(content)


receive_address.send_keys("1771856179@qq.com")



















    


















































































# from selenium import webdriver  
# import os  
# from selenium.webdriver.common.by import By  
# from selenium.webdriver.support.ui import WebDriverWait  
# from selenium.webdriver.support import expected_conditions as EC  
  
# # 根据操作系统选择清屏命令（可选）  
# clear_command = "cls" if os.name == "nt" else "clear"  
# os.system(clear_command)  # 清屏（可选，通常不推荐在脚本中使用）  
  
# url = "https://mail.whut.edu.cn/"  
# options = webdriver.EdgeOptions()  
# options.add_experimental_option("detach", True)  # 浏览器在脚本执行完毕后保持打开状态  
  
# try:  
#     browser = webdriver.Edge(options=options)  
#     browser.get(url=url)  
      
#     # 如果需要等待页面加载完成，可以使用以下代码（示例）  
#     # wait = WebDriverWait(browser, 10)  # 等待最多10秒  
#     # element = wait.until(EC.visibility_of_element_located((By.ID, "some_element_id")))  # 等待某个元素可见  
  
# except Exception as e:  
#     print(f"An error occurred: {e}")  
# finally:  
#     # 注意：由于设置了detach选项，这里不会关闭浏览器  
#     # 如果需要关闭浏览器，请注释掉detach选项或在其他地方调用browser.quit()  
#     pass
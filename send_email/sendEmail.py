
import  smtplib  #smtplib用于发送邮件，email用于编写邮件内容
                 #邮件对象MIMEMultipart

#发送MIMEText文本内容的邮件，文本类型：
    #普通文本plain。超文本html，二进制文本txt，xlsx，html等
    #语法：MIMEText（文字内容，文本类型，编码方式）
from email.mime.text import MIMEText  

#创建邮件对象
from email.mime.multipart import MIMEMultipart

#定义主题（包括标题）
from email.header import Header

import schedule,time

def job():
    from_email="cran177@163.com"#发件人
    pass_code="AJrsdjwsRg49jGen"#授权码，到邮箱设置里找
    to_email="3341444569@qq.com"#收件人
    title="hello"#邮件的标题
    email_body="my name is rg"#文件主体的内容
    send_email(from_email,pass_code,to_email,title,email_body)



def send_email(from_email,pass_code,to_email,title,email_body):

    #创建邮件对象
    msg=MIMEMultipart()

    #语法Header（标题，编码方式）
    subject=Header(title,"utf-8").encode()
    #将msg中的主题（标题）赋值为subject
    msg["Subject"]=subject
    #设置发件人
    msg["From"]=from_email
    #设置收件人
    msg["To"]=to_email

    #设置主体body中的数据
    body=MIMEText(email_body,"plain","utf-8")
    #将这些数据加入到msg中
    msg.attach(body)

    #连接邮箱服务器：SMTP_SSL协议（安全邮件传输协议），参数为：服务器地址和端口（邮箱中去找）
    with smtplib.SMTP_SSL("smtp.163.com", 465) as smtp:
        #登录发件人邮箱（利用收件人邮箱和授权码登陆）
        smtp.login(from_email, pass_code)
        #发送邮件
        smtp.send_message(msg)
   


def  delay_time():#用来定时发送邮件,利用schedule模块
    schedule.every(1).seconds.do(job)#每隔1秒钟执行job函数
    #schedule.every().day.at("8:39").do(job) #定时每天八点39执行job

    while True:
        # 这是  schedule  库的一个方法，用于检查并执行所有待执行的任务。如果有任务的执行时间到了，它会立即执行这些任务。
        schedule.run_pending()

        #这行代码使程序暂停 1 秒钟。这样做的目的是减少 CPU 的使用率，让程序在每次循环之间等待，而不是不断地快速循环。
        time.sleep(1)
        print("发送成功")




def main():
    job()
    delay_time()


if __name__=="__main__":
    main()
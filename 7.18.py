import re


#1
# def format_string(n):
#     return f'{n:02d}'


# date=re.compile(r"^\d{1,2}/\d{1,2}/\d{4}$")
# date_input=input("输入要检测的日期：")
# date_check=date.search(date_input)

# try:
#     date_check_list=date_check.group().split('/')
# except:
#     print("日期格式错误")
#     quit()

# count=0  
# day,month,year=date_check_list
# date_right=[]
# if (1<=int(day) and int(day)<=31):
#     day=format_string(int(day))
#     date_right.append(day)
#     count+=1
#     if (1<=int(month) and int(month)<=12):
#         month=format_string(int(month))
#         date_right.append(month)
#         count+=1
#         if (1000<=int(year) and int(year)<=2999):
#             year=format_string(int(year))
#             date_right.append(year)
#             date_r='/'.join(date_right)
#             count+=1
#             print(f'日期  {date_r}  格式正确')
# if count!=3:
#     print('日期不是有效日期')




#2
def qaing(strings):
    string=re.compile(r'[a-zA-Z0-9]{8,}')
    D=re.compile(r'')
                    
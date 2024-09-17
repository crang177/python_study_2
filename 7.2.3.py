import re

IdNumberRegex=re.compile(r'\d{4}-\d{3}-\d{3}')
a=IdNumberRegex.search(input('请输入你的学号:'))
try: 
    print('我的学号是：'+a.group())
except AttributeError:
    print('学号格式不正确') 


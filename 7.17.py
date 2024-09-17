import re

#20
# a=re.compile(r'^(?:\d{1,3}(?:,\d{3})*)?$')
# #a=re.compile(r'\d\d')
# b=a.search('2,222')
# print(b)
# try:    
#     print(b.group())
# except :
#     print('格式不对')



#21
# a=re.compile(r'[A-Z](\w)* Nakamoto')
# b=a.search('Sadfs')
# try:
#     print(b.group())
# except:
#     print('错误')



#22
a=re.compile(r'^(Alice|Bob|Carol)(\s+)(eats|pets|throws)(\s+)(apples|cats|baseballs)(.)$',re.IGNORECASE)
b=a.findall('bob     Pets            apples.')
if b:
    for i in b:
        i=list(i)
        print(''.join(i))
else:
    print('错误')

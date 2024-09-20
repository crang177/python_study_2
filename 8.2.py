#如何让人忙几小时

import pyinputplus as pyip
# while True:
#     a=pyip.inputYesNo(prompt='你是否想知道如何让人忙几小时:',
#                       allowRegexes=[r'si',r's'])
#     if a=='no':
#         break

cheese=[['cheddar','swiss','mozzarella'],[3,2,1]]
n=0
expense2=0
answer=pyip.inputYesNo(prompt="是否需要奶酪(y,yes或者n,no): ")
if answer=='yes':
    cheese_type_num=pyip.inputMenu(cheese[0],prompt='请输入你要的奶酪类型:\n',numbered=True)
    # for i in cheese[0]: 
    #     if i==cheese_type_num:
    #         expense2+=cheese[1][n]
    #         break
    #     n+=1
print()

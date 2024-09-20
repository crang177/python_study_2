import pyinputplus as pyip
import time 
import re
import os


#8.6.1   三明治机
def ClearScreen(n):
    time.sleep(n)
    os.system('cls')

def gotoxy(m,n):
    print(f'\033[{n};{m}H',end='')

def PriceMenu():
    print('                   价格表    ')
    print('面包类：')
    for i,item in enumerate(bread[0]):
        print(f"  {item}------{bread[1][i]}元")   
    print('蛋白质类：')
    for i,item in enumerate(protein[0]):
        print(f"  {item}------{protein[1][i]}元") 
    print('奶酪：')
    for i,item in enumerate(cheese[0]):
        print(f"  {item}------{cheese[1][i]}元") 
    print('蔬菜：')
    for i,item in enumerate(vegetable[0]):
        print(f"  {item}------{vegetable[1][i]}元") 
    print('\n\n')

def ChooseBread():
    ClearScreen(0.5)
    PriceMenu()
    bread_type_num=pyip.inputMenu(bread[0],prompt='请输入面包的类型\n',numbered=True)
    n=0
    expense1=0
    for i in bread[0]: 
        if i==bread_type_num:
            expense1+=bread[1][n]
            print(f'{bread_type_num}    {expense1}元')
            break
        n+=1
    print()
    return expense1

def ChooseProtein():
    ClearScreen(0.5)
    PriceMenu()
    protein_type_num=pyip.inputMenu(protein[0],prompt='请输入蛋白质的类型\n',numbered=True)
    n=0
    expense1=0
    for i in protein[0]: 
        if i==protein_type_num:
            expense1+=protein[1][n]
            print(f'{protein_type_num}  {expense1}元')
            break
        n+=1
    print()
    return expense1

def ChooseCheesseOrNot():
    n=0
    expense2=0
    answer=pyip.inputYesNo(prompt="是否需要奶酪(y,yes或者n,no): ")
    if answer=='yes':
        cheese_type_num=pyip.inputMenu(cheese[0],prompt='请输入你要的奶酪类型:\n',numbered=True)
        for i in cheese[0]: 
            if i==cheese_type_num:
                expense2+=cheese[1][n]
                print(f'{cheese_type_num}   {expense2}元')
                break
            n+=1
    print()
    return expense2

def ChooseVegetableOrNot():
    n=0
    expense3=0
    answer=pyip.inputYesNo(prompt="是否需要蔬菜(y,yes或者n,no): ")
    if answer=='yes':
        vegetable_type_num=pyip.inputMenu(vegetable[0],prompt='请输入你要的蔬菜类型:\n',numbered=True)
        for i in vegetable[0]: 
            if i==vegetable_type_num:
                expense3+=vegetable[1][n]
                print(f'{vegetable_type_num}    {expense3}元')
                break
            n+=1
    print()
    return expense3
        
ClearScreen(0.01)
sandwich_type=['面包类','蛋白质类']
bread=[['wheat','white','sourdough'],[1,2,3]]
protein=[['chicken','turkey','ham','tofu'],[4,3,2,1]]
cheese=[['cheddar','swiss','mozzarella'],[3,2,1]]
vegetable=[['mayo','mustard','lettuce','tomato'],[1,2,3,4]]
expense=0






#主函数
PriceMenu()
sandwich_type_num=pyip.inputMenu(sandwich_type,prompt='请输入你要的三明治类型\n',numbered=True)
if sandwich_type_num=='面包类':
    expense+=ChooseBread()
else:
    expense+=ChooseProtein()
signal=ChooseCheesseOrNot()
expense+=signal
signal=ChooseVegetableOrNot()
expense+=signal
number=pyip.inputInt('请输入你要的个数：')
print(f'总共需要支付：{number} X {expense} = {number*expense} 元')




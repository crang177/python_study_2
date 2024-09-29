#选择性复制

import os,time,re,shutil
from pathlib import Path
import pyinputplus as pyip

def check_folder(name):
    folder_name_list=os.listdir("D:\\py exercise file")
    for i in folder_name_list:
        if i==name:
            print('该文件已存在')
            quit()
    

os.system("cls")
a=pyip.inputStr(prompt="请输入要复制的路径：")
print()
path=Path(a)
path2=Path("D:\\py exercise file")
check_folder('txt-format')
os.makedirs(path2/'txt-format')
for folder,subfolders,filenames in os.walk(a):
    path1=Path(folder)
    search_format_list=list(path1.glob('*.txt'))
    for i in search_format_list:
        shutil.copy(path1/i,path2/'txt-format')
print(f"复制路径{a}处的.txt文件成功")
print(f"复制到了路径{path2/'txt-format'}")

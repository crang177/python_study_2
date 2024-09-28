#将一个文件夹备份到一个ZIP文件

import zipfile,os,re,os.path,time
from ansilib import ansi
from pathlib import Path
import pyinputplus as pyip



#检查zip文件名的名字是否存在
# def check_zip(path):
#     numRegexes=re.compile(r'\d+')
#     nameRegexes=re.compile(r'^.*\d+.zip$')
#     max=0
#     namelist=os.listdir(path)
#     for i in namelist :
#         match1=nameRegexes.search(i)
#         if match1:
#             match2=numRegexes.search(match1.group())
#             if  max < int(match2.group()):
#                 max=int(match2.group())
#    return max+1

#检查zip文件名的名字是否存在
def check_name_zip(Name):
    os.system('cls')
    path1=Path('D:\\py exercise file')
    namelist=os.listdir('D:\\py exercise file')
    for i in namelist:
        if i==name:
            print("该压缩文件已存在")
            print(f'路径：{path1/Name}\n')
            time.sleep(5)
            quit()
        


#压缩文件函数
def change_zip(path,Name):
    os.system('cls')
    #n=check_zip('D:\\py exercise file')
    #NumName=f'AlsPythonBook{n}.zip'
    path1=Path('D:\\py exercise file')
    AlsPythonBookZip=zipfile.ZipFile(path1/Name,'a')
    for folder,subfolders,filenames in os.walk(path):
        for filename in filenames:
            AlsPythonBookZip.write(folder+'\\'+filename,compress_type=zipfile.ZIP_DEFLATED)
    print(f"压缩文件{Name}成功")
    print(f'路径：{path1/Name}\n')



os.system('cls')
prompt="请输入要压缩的文件的路径："
path=pyip.inputStr(prompt)
name=f'{os.path.basename(path)}.zip'
check_name_zip(name)
change_zip(path,name)
time.sleep(5)



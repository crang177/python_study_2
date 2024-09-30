#删除不需要的文件

import shutil,os,os.path,re
from pathlib import Path
import pyinputplus as pyip
import send2trash



os.system("cls")
a=pyip.inputStr(prompt='请输入要清理的路径：')

#删除整个文件夹及其子文件夹和子文件
# a_list=a.split('\\')
#shutil.rmtree(Path(a_list[0]+'\\'+a_list[1]+'\\'+a_list[2]+'\\'+a_list[3]+'\\'+a_list[4]))


#删除文件夹中指定大小的文件。size为字节
for folder,subfolders,filenames in os.walk(a):
    for i in filenames:
        size=os.path.getsize(Path(folder)/i)
        if size>= 1024:
            print(f"要删除文件的绝对路径:{Path(folder)/i}\n")
            # os.unlink(Path(folder)/i)      #永久删除
            send2trash.send2trash(Path(folder)/i)  #将文件发送到计算机的回收站，文件可恢复



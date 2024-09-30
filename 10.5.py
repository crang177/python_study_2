

import zipfile,os,re,os.path,time
from ansilib import ansi
from pathlib import Path
import pyinputplus as pyip


#检查压缩zip文件名的名字是否存在
def check_name_zip(Name):
    os.system('cls')
    path1=Path('D:\\py exercise file')
    namelist=os.listdir('D:\\py exercise file')
    for i in namelist:
        if i==Name:
            print("该压缩文件已存在")
            print(f'路径：{path1/Name}\n')
            time.sleep(5)
            quit()
        


#压缩文件函数
def change_zip(path,name):
    os.system('cls')
    shotname=name[:len(name)-4]
    AlsPythonBookZip=zipfile.ZipFile(Path('D:\\py exercise file')/name,'a')
    for folder,subfolders,filenames in os.walk(path):
        relative_root=os.path.relpath(folder,path)
        for filename in filenames:
            file_path=os.path.join(folder,filename)

            archive_path=os.path.join(shotname,relative_root,filename)
            AlsPythonBookZip.write(file_path,compress_type=zipfile.ZIP_DEFLATED,arcname=archive_path)
    AlsPythonBookZip.close()
    print(f"压缩文件{name}成功")
    print(f'路径：{Path('D:\\py exercise file')/name}\n') 



#解压函数
def uncompress(path):
    path1=Path('D:\\py exercise file')
    path2=Path(path)
    basename=os.path.basename(path)
    uncompress_file=zipfile.ZipFile(path2)
    check_uncompress_folder_name(basename[:len(basename)-4])
    uncompress_file.extractall(path1/basename[:len(basename)-4])
    print(f"解压成功，解压路径{path1/basename[:len(basename)-4]}\n")
    time.sleep(5)


#检查解压函数得到的文件夹是否存在
def check_uncompress_folder_name(name):
    folder_name_list=os.listdir("D:\\py exercise file")
    for i in folder_name_list:
        if i==name:
            print("该压缩文件已存在")
            print(f'路径：{"D:\\py exercise file"+name}\n')
            time.sleep(5)
            quit()



def main():
    os.system('cls')
    print("压缩文件输入:1         解压文件输入:2")
    n=pyip.inputInt(prompt="    你的选择:",allowRegexes=r'^1|2$')
    print()
    if n==1:
        prompt="请输入要压缩的文件的路径："
        path=pyip.inputStr(prompt)
        name=f'{os.path.basename(path)}.zip'
        check_name_zip(name)
        change_zip(path,name)
        time.sleep(5)
    else:
        path=pyip.inputStr(prompt="请输入要解压文件的路径：",allowRegexes=r'^.*.zip$')
        uncompress(path)





main()




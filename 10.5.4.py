import zipfile,os,re,os.path,time
from ansilib import ansi
from pathlib import Path
import pyinputplus as pyip



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



os.system('cls')
prompt="请输入要压缩的文件的路径："
path=pyip.inputStr(prompt)
name=f'{os.path.basename(path)}.zip'
change_zip(path,name)
time.sleep(5)

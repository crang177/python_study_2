#解压归档文件Zip

import zipfile,os,re,os.path,time
from ansilib import ansi
from pathlib import Path
import pyinputplus as pyip


def uncompress(path):
    path1=Path('D:\\py exercise file')
    path2=Path(path)
    basename=os.path.basename(path)
    uncompress_file=zipfile.ZipFile(path2)
    uncompress_file.extractall(path1/basename[:len(basename)-4])
    print(f"解压成功，解压路径{path1/basename[:len(basename)-4]}\n")
    time.sleep(5)

os.system('cls')
path=pyip.inputStr(prompt="请输入要解压文件的路径：",allowRegexes=r'^.*.zip$')
uncompress(path)
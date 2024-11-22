import os,shutil
import requests

def change_name():
    ls=os.listdir("D:\\music\\music_jiami")
    for i in ls:
        if i[-5:]==".flac":
            shutil.move("D:\\music\\music_jiami"+"\\"+i,"D://music//music_jiami"+"\\"+i[:-5])

def change_type():
    res=requests.get


if __name__=="__main__":
    os.system("cls")
    # change_name()
#将带有美国日期风格日期的文件重命名为中国日期风格
from pathlib import Path
import  os,shutil,re
from ansilib import ansi


def printf(i,date_change):
    print('文件',end='')
    ansi.text_color(31)
    print(f'{i}',end='')
    ansi.text_reset()
    print('的名字已经更改为',end='')
    ansi.text_color(31)
    print(f'{date_change}\n')
    ansi.text_reset()



os.system('cls')
path=Path('.\\')
English_dateRegexes=re.compile(r'\d{2}-\d{2}-\d{4}')
file_name_list=os.listdir('.\\')
month1=[1,3,5,7,8,10,12]
month2=[4,6,9,11]
c=0
for i in file_name_list:
    match1=English_dateRegexes.search(i)
    if match1:
        date_list=match1.group().split('-')
        
        if int(date_list[1]) in month1:
            if 1<=int(date_list[0]) and  int(date_list[0])<=31:
                pass
            else:
                continue
        elif int(date_list[1]) in month2:
            if 1<=int(date_list[0]) and  int(date_list[0])<=30:
                pass
            else:
                continue
  
        elif int(date_list[1]) ==2 :
            if (int(date_list[2])%400==0 or (int(date_list[2])%4==0 and int(date_list[2])%100!=0)):
                if 1<=int(date_list[0]) and  int(date_list[0])<=29:
                    pass
                else:
                    continue
            else:
                if 1<=int(date_list[0]) and  int(date_list[0])<=28:
                    pass
                else:
                    continue
    
        count=0
        k=0
        date_change_list=[]
        while(count<=len(i)-1)    :
            if i[count:count+10]  == ('-'.join(date_list)) :
                date_list.reverse()
                date_string='-'.join(date_list)
                for j in range(10):
                    date_change_list.append(date_string[j])
                    count+=1
                k=1
                c+=1
            date_change_list.append(i[count])
            count+=1  
        date_change=''.join(date_change_list)
        shutil.move(i,date_change)
        printf(i,date_change)
        
if c==0:
    ansi.text_color(35)
    print('所有文件中不包含美国日期风格')  
    ansi.text_reset()





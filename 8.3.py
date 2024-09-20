#乘法测验(10个问题)

import pyinputplus as pyip
import random
import time
import os

numberofQuestions=10
correctAnswers=0
for i in range(numberofQuestions):
    num1=random.randint(10,20)
    num2=random.randint(10,20)
    prompt='第 %s 题的数学计算式为%s X %s = '%(i+1,num1,num2)

    try:
        pyip.inputStr(prompt,allowRegexes=[r'^%s$'%(num1*num2)],blockRegexes=[r'.*','Incorrect!'],limit=3,timeout=8)
    except pyip.TimeoutException:
        print("时间到了")
    except pyip.RetryLimitException:
        print('达到最大错误次数')
    else:
        print('答案正确')
        correctAnswers+=1
    time.sleep(1)
    print()
print("准确率：%s /%s = %s"%(correctAnswers,numberofQuestions,round(correctAnswers/numberofQuestions,2)))
time.sleep(3)
os.system('cls')
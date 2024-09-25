import shelve
import random
import os
import pyinputplus as pyip
#生成随机的测验试卷

os.system('cls')
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 
            'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 
            'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 
            'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 
            'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City', 
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 
            'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 
            'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 
            'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 
            'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville',
            'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier',
            'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston',
            'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
n=pyip.inputInt(prompt='请输入要生成多少份试卷：')
for quizNum in range(n):
    quizFile=open(f'9_5_quiz{quizNum+1}.txt','w',encoding='utf-8')
    answerkeyFile=open(f'9_5_quiz_answer{quizNum+1}.txt','w',encoding='utf-8')

    quizFile.write("名字:\n\n日期:\n\n成绩:\n\n")
    quizFile.write((' '*12)+f'州的首府名字卷子(第 {quizNum+1} 卷)')
    quizFile.write('\n\n')

    states=list(capitals.keys())
    random.shuffle(states)

    for questionNum in range(40):
        correctAnswers=capitals[states[questionNum]]
        wrongAnswers=list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        AnswersOptions=list(random.sample(wrongAnswers,3))
        AnswersOptions.append(correctAnswers)
        random.shuffle(AnswersOptions)
      
        quizFile.write(f"{questionNum+1}州{states[questionNum]}的首府是(  )\n")
      
        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}.{AnswersOptions[i]}\n")
            if AnswersOptions[i]==correctAnswers:
                answer_right='ABCD'[i]
        quizFile.write("\n")
        answerkeyFile.write(f' {questionNum+1}.{answer_right}\n')

quizFile.close()
answerkeyFile.close()
    
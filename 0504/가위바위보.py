import random

#나 랑 컴퓨터
#이겼을때
#졌을때
#비김
a=['가위','바위','보']

Computer=random.choice(a)
User=input()

print(Computer)

if Computer=='가위' and User=='바위' or\
    Computer=='바위' and User=='보' or\
    Computer=='보' and User=='가위':
        print("이겼습니다")
elif User=='가위' and Computer=='바위' or\
    User=='바위' and Computer=='보' or\
    User=='보' and Computer=='가위':
        print('lose')
else:
        print('draw')












import random

a=random.randint(1,30) #1에서 30까지 임의의 정수를 불러 a에 저장한다.
b=random.randint(1,30) #1에서 30까지 임의의 정수를 불러 b에 저장한다.

print(a,"+",b,"=") #문제를 출력합니다.
x=input() #답을 입력받아 x에 저장합니다. 문자열로 저장됩니다.
c=int(x) #문자열로 되어 있는 x를 정수로 바꾸어 c에 저장합니다.

if a+b==c:
    print("천재")
else:
    print("바보")

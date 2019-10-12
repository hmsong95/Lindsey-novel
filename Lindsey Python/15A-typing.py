import random
import time

w=["cat","dog", "fox", "monkey", "mouse", "panda", "frog", "snake", "wolf"]
n=1 #문제 번호
print("[타자게임] 준비 되면 엔터!")
input() #사용자가 엔터를 누를때까지 기다립니다.
start=time.time() #시간 기록을 시작합니다.

q=random.choice(w)
while n<=5: #문제를 다섯번 반복합니다.
    print("문제",n)
    print(q) #문제를 보여줍니다.
    x=input() #사용자 입력을 받습니다.
    if q==x:
        print("통과") #문제와 입력이 같으면 "통과"라고 출력합니다.
        n=n+1 #문제 번호 1을 증가시킵니다.
        q=random.choice(w)
    else:
        print("오타! 다시 도전!")

end=time.time() #끝난 시간을 측정합니다.
et=end-start
et=format(et, ".2f") #보기 좋게 소수점 두자리만 표기합니다.
print("타자시간:", et,"초")

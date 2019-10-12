import random

n=random.randint(1,30) #1에서 30까지 임의의 수를 뽑습니다.

while True: #답을 맞출때까지 반복합니다.
    x=input("맞혀보세요")
    g=int(x) #입력 받은 값을 비교할 수 있도록 정수로 바꿉니다.

    if g==n: #사용자가 추측한 값과 임의의 값이 같으면 정답
        print("정답")
        break #정답을 맞추면 break를 써서 while 반복을 빠져 나갑니다.

    if g<n:
        print("너무 작아요")

    if g>n:
        print("너무 커요")
    

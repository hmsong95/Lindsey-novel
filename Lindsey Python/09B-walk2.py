import turtle as t
import random

t.shape("turtle") #거북이 모양의 거북이 그래픽을 사용합니다.
t.speed(0) #거북이 속도를 가장 빠르게 설정합니다.

for x in range(500):
    a=random.randint(1,360) #1에서 360까지의 숫자 중, 임의의 정수를 a에 저장한다.
    t.seth(a) #거북이 방향을 a 각도로 돌립니다.
    b=random.randint(1,20) #1에서 20사이의 정수를 b에 저장합니다.
    t.fd(b) #거북이가 b만큼 앞으로 갑니다.
    

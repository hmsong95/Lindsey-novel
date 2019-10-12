import turtle as t
import random

def turn_up():
    t.left(2) #거북이를 왼쪽으로 2도 돌립니다.

def turn_down():
    t.right(2) #거북이를 오른쪽으로 2도 돌립니다.

def fire(): #Spacebar를 누르면 거북이 대포를 발사합니다.
    ang=t.setheading() #현재 거북이가 바라보는 각도를 기억합니다.
    while t.ycor() >0: #거북이가 땅 위에 있는 동안 반복합니다.
        t.forward(15)
        t.right(5)

    #while 반복문을 빠져나오면 거북이가 땅에 닿은 상태입니다.
    d=t.distance(target,0) #거북이와 목표 지점과의 거리를 구합니다.
    t.sety(random.randint(10,100) #성공 또는 실패를 표시할 위치를 지정합니다.
    if d<25: #거리 차이가 25보다 작으면 목표 지점에 명중한 것으로 처리
           t.color("blue")
           t.write("Good", False, "center", ("", 15)
           t.color("black") #거북이의 색을 블랙으로 다시 되돌립니다.
           t.goto(-200, 10) #거북이 위치를 처음 발사했던 곳으로 되돌립니다.
           t.setheading(ang) #각도도 처음 기억해 둔 각도로 되돌립니다. 
                   

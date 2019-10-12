import turtle as t

def polygon(n):
    for x in range(n): #n번 반복합니다.
        t.fd(50) #거북이가 50만큼 앞으로 갑니다.
        t.lt(360/n) #거북이가 360/n만큼 왼쪽으로 회전합니다.

def polygon2(n,a):
    for x in range(n):
        t.fd(a) #거북이를 a 만큼 이동합니다.
        t.lt(360/n)

polygon(3) #3각형을 그립니다.
polygon(5) #5각형을 그립니다.

#그림을 그리지 않고 거북이를 100만큼 이동합니다.
t.up()
t.forward(100)
t.down()

polygon2(3,75) #한 변이 75인 삼각형을 그립니다.
polygon2(5, 100) #한 변이 100인 5각형을 그립니다. 

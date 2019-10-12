import turtle as t
n=50 #원을 50개 그립니다.
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80) #현재 위치에서 반지름이 80인 원을 그립니다.
    t.lt(360/n) #거북이가 360/n만큼 왼쪽으로 회전합니다. 

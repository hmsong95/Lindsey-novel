import turtle as t
angle=89 #거북이가 왼쪽으로 회전할 각도를 지정합니다.
t.bgcolor("black")
t.color("yellow")
t.speed(0)
for x in range(200):
    t.fd(x)
    t.lt(angle)
    

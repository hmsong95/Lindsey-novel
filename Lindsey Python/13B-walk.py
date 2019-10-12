import turtle as t

def turn_right(): #오른쪽으로 이동하는 함수
    t.setheading(0)
    t.fd(10)

def turn_up(): #위로 이동하는 함수
    t.seth(90)
    t.fd(10)

def turn_left(): #왼쪽으로 이동하는 함수
    t.seth(180)
    t.fd(10)

def turn_down() : #아래로 이동하는 함수
    t.seth(270)
    t.fd(10)

def blank(): #화면을 지우는 함수
    t.clear()

t.shape("turtle")
t.speed(0)
t.onkeypress(turn_right, "Right") #오른쪽 화살표를 누르면 turn_right 함수를 시작합니다.
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(blank, "Escape") #ESC를 누르면 blank 함수가 실행
t.listen() #거북이 그래픽 창이 키보드 입력을 받습니다.


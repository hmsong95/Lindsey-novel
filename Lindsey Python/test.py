import turtle as t

t.color("red")
t.begin_fill()
n=4
for x in range(4):
    t.fd(100)
    t.lt(360/n)
t.end_fill()



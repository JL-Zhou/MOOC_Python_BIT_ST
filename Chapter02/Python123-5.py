#Python123-5.py
import turtle as t
t.pensize(5) 
for i in range(4):
    t.seth(90 * i)  # 回到原点要转90度
    t.fd(150)
    t.right(90)
    t.circle(-150, 45)
    t.goto(0,0)
t.done()
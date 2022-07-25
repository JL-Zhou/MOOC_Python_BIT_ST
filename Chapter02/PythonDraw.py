#PythonDraw.py
import turtle
turtle.setup(650, 350, 200, 200)  #(width,height,startx,starty)
turtle.penup()                    #提起画笔
turtle.fd(-250)                   #沿着当前方向前进指定距离-250
turtle.pendown()                  #放下画笔
turtle.pensize(25)                #设置画笔线条的粗细为25
turtle.pencolor("purple")
turtle.seth(-40)                  #修改画笔的横坐标到-40，纵坐标不变
for i in range(4):
    turtle.circle(40, 80)         #绘制一个指定半径40和角度80的圆或弧形
    turtle.circle(-40, 80)
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()


#width:窗口宽度。如果值是整数，表示像素值；如果值是小数，表示窗口宽度与屏幕的比例
#height:窗口高度。如果值是整数，表示像素值；如果值是小数，表示窗口高度与屏幕的比例
#startx：窗口左侧与屏幕右侧的像素距离。如果值是None，窗口位于屏幕水平正中央。
#starty：窗口顶部与屏幕顶部的像素距离。如果值是None，窗口位于屏幕垂直正中央。
#StarDraw.py
#这道题不对 中间是空心的
from turtle import *      #与import turtle导包不同、声明不同、路径不同
color ('red', 'red')      #分别是pencolor和fillcolor对应的颜色
begin_fill()
for i in range(5):
    fd(200)               #像素距离
    rt(144)               #向右旋转144度
end_fill()
done()                    #画板停留
#StarDraw3.py
# 未解决：把turtle转为png
from turtle import * 
color ('red', 'red')
begin_fill()
for i in range(5):
    fd(200)
    lt(72)
    fd(200)
    rt(144)
end_fill()
done()
ts = getscreen()
ts.getcanvas().postscript(file="Star.png")
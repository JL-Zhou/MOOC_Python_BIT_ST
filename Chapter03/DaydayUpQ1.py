#DayDayUpQ1.py
dayup =pow(1.001, 365) #pow函数表示幂运算 pow(x,y)表示x的y次幂，pow(x,y,z)表示x的y次幂后除z的余数
daydown =pow(0.999, 365)
print("向上：{:.2f}, 向下：{:.2f}".format(dayup, daydown))

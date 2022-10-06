#DaydayUpQ4.py
def dayUP(df):    #def定义dayUP函数
    dayup = 1
    for i in range(365):
        if i % 7 in[6,0]:
            dayup = dayup*(1 - 0.01)  #在周末
        else:
            dayup = dayup*(1 + df)  #在工作日加df
    return dayup
dayfactor = 0.01
while dayUP(dayfactor) < 37.78:   #1.01^365 = 37.78
    dayfactor += 0.001
print("工作日的努力参数是: {:.3f}".format(dayfactor))
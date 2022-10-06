#DaydayUpQ3.py
dayup =1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:   #计算是否在工作日#
        dayup = dayup*(1-dayfactor)   #如果i在休息日，则退步0.01
    else:
        dayup = dayup(1+dayfactor)      #如果i在工作日1-5，则进步0.01
print("工作的力量：{:.2f}".format(dayup))
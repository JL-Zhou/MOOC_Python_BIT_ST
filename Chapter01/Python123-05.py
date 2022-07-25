#Python123-05.py
#人民币和美元间汇率固定为：1美元 = 6.78人民币
#程序可以接受人民币或美元输入，转换为美元或人民币输出。人民币采用RMB表示，美元USD表示，符号和数值之间没有空格
MoneyStr = input()
if MoneyStr[3:] in ['RMB']:
    USD = eval(MoneyStr[:3]) / 6.78
    print("{:.2f}USD".format(USD))
elif MoneyStr[3:] in ['USD']:
    RMB = eval(MoneyStr[:3]) * 6.78
    print("{:.2f}RMB".format(RMB))
else:
    print("输入格式错误")

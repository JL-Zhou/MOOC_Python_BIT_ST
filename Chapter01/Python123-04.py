#Python123-04.py
#(1) 输入输出的摄氏度采用大写字母C开头，温度可以是整数或小数，如：C12.34指摄氏度12.34度；
#(2) 输入输出的华氏度采用大写字母F开头，温度可以是整数或小数，如：F87.65指华氏度87.65度；
#(3) 不考虑异常输入的问题，输出保留小数点后两位；
#(4) 使用input()获得测试用例输入时，不要增加提示字符串。

TempStr = input()
if TempStr[0] in ['F']:
    C = (eval(TempStr[1:]) - 32)/1.8     #TempStr[1:]表示字符串除首字符外的所有字符
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[0] in ['C']:
    F = 1.8 * eval(TempStr[1:]) + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
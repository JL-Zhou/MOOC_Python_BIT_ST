#TempConvert.py
TempStr = input("请输入带有符合的温度值：")
if TempStr[-1] in ['f','F']:          #华氏度转摄氏度 不分大小写  #eval()评估函数 qu
    C = (eval(TempStr[0:-1]) - 32)/1.8      # （F -32）/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['c', 'C']:       #摄氏度转华氏度 不分大小写
    F = 1.8 * eval(TempStr[0:-1]) + 32     # 1.8 * c + 32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")
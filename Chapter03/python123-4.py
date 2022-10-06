#python123-4.py
n = eval(input())  #输入一个整数N，N为奇数
for i in range(1, n+1, 2):
    print("{0:^{1}}".format('*'*i, n)) #{1}为占位符，代替后面的n，{0:^{1}}中表示宽度是n
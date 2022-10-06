#Caesar Cipher
p = input() #输入字符串p
t = ""   #定义空字符串t
for c in p:
    if 'a' <= c <= 'z':   #字符c在a-z中
        t += chr( ord('a') + ((ord(c)-ord('a')) + 3 ) % 26 )  # C=(P+3) mod 26，结果添加到字符串t上
    elif 'A' <= c <= 'Z': #字符c在A-Z中
        t += chr( ord('A') + ((ord(c)-ord('A')) + 3) % 26 )
    else:  #字符c属于其他
        t += c
print(t)

# 思路：for 循环遍历字符串，分类判定后将结果添加到空字符串t上
# ord()将字符串转为Unicode码，转码之后将序数进行四则运算，得出加密后的字符Unicode码
# %26 是防止数值溢出，保证数值在 a - z 之间循环
# chr() 将Unicode码转为其对应的字符串
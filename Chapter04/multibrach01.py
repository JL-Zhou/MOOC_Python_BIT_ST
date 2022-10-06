#multibrach01.py
score = eval(input())
if 0 <= score <= 60:
    grade = "D"
elif 61 <= score <= 70:
    grade = "C"
elif 71 <= score <= 80:
    grade = "B"
elif 81 <= score <= 100:
    grade = "A"
print("输入成绩属于级别{}".format(grade))



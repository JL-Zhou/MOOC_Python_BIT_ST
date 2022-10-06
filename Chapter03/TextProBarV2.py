#TextProBarV2.py
import time
for i in range(101):
    print("\r{:3}%".format(i), end="")  #打印后光标退回到之前的位置\r
    time.sleep(0.1)
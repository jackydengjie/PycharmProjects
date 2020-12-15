import cv2
import  os
import time
from threading import Thread
import numpy as np

name=r"aaa.png"

print(name)

#打开摄像头
capture=cv2.VideoCapture(700)

for i in range(1,8):
    print(i)
    ret, frame = capture.read()
    cv2.imshow('image', frame)
    cv2.waitKey(1000)
    cv2.destroyWindow('image')

cv2.imwrite('qq.png',frame)
name2=r"qq.png"
print(name2)
difference = cv2.subtract(name2, name)
print("----------------")
result = not np.any(difference)
if result is True:
     print("两张图片一样")
else:
     cv2.imwrite("result.jpg", difference)
     print ("两张图片不一样")





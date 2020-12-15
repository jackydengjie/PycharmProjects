# 人脸识别
import cv2
import  os
import time
from face_recognition import get_similarity
from threading import Thread


name=r"aaa.png"

def recognition():
    print(1)
    time.sleep(5)
    #对两张图片进行对比 第一个参数是图片文件，第二个参数是拍照的图片二进制数据
    score = get_similarity(name,frame_data)
    if score and score>=90:
        print(2)
        with open(r"123.txt","a",encoding="utf-8") as f:
            f.write(name+"=>"+time.ctime()+"\n")
        print("打卡成功！")
    else:
        print(3)
        print("识别错误！")


Thread(target=recognition).start()


#打开摄像头
capture=cv2.VideoCapture(700)
# width = 640
# height = 480
# w = 360
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# crop_w_start = (width-w)//2
# crop_h_start = (height-w)//2

while True:
    #拍照
    ret,frame=capture.read()
    # frame = frame[crop_h_start:crop_h_start + w, crop_w_start:crop_w_start + w]

    #把frame转换成二进制
    frame_data=cv2.imencode(".png",frame)[1].tobytes()
    #print(frame_data)

    #图像展示
    cv2.imshow('face',frame)

    #设置退出的条件
    if cv2.waitKey(1)== ord('q'):
        print(4)
        #9表示强制退出
        os.kill(os.getpgid(),9)




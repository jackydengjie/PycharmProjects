# je=int(input('请输入奖金金额：'))
# print('你输入的奖金金额是：',je)
#
# if je<=100000:
#     jj=je*0.1
# elif je>100000 and je<200000:
#     jj=(je-100000)*0.075+100000*0.1
#
# print(jj)

import cv2
ID = 1
while(1):
    cap = cv2.VideoCapture(ID)
    # get a frame
    ret, frame = cap.read()
    if ret == False:
        ID += 1
    else:
        print(ID)
        break

# cap =cv2.VideoCapture(700)
# width = 640
# height = 480
# w = 360
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
# crop_w_start = (width-w)//2
# crop_h_start = (height-w)//2
#
# if(cap.isOpened()):
#     print(1)
# else:
#     print(2)


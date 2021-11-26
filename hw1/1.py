import numpy as np
import cv2
import sys
import os

imglist = []	#存储图片
filedir = sys.argv[1]	#图片目录
filelist = os.listdir(filedir)	#目录下的文件列表

#提取出目录下的视频
for filename in filelist:
    if os.path.splitext(filename)[1]=='.avi':
        video = cv2.VideoCapture(os.path.join(filedir,filename))
        #获取视频的尺寸及帧率
        size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        fps = int(video.get(cv2.CAP_PROP_FPS))
        fourcc = video.get(cv2.CAP_PROP_FOURCC)

#文字内容及位置
text = "3190102780 Wang Yiming"
textPos = (int(size[0]/2)-200, size[1]-50)

#提取出目录下的图片
for filename in filelist:
    if os.path.splitext(filename)[1]=='.jpg':
        img = cv2.imread(os.path.join(filedir,filename))
        img = cv2.resize(img, dsize=size)
        cv2.putText(img, text, textPos, cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 200, 200), 2)
        imglist.append(img)

#确定视频格式并初始化
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
videoWrite = cv2.VideoWriter( '1.avi', fourcc, fps, size )

#将图片依次添加进视频
for i in range(len(imglist)-1):
    img1 = imglist[i]
    img2 = imglist[i+1]
    #展示图片
    for wait in range(fps):
        videoWrite.write(img1)
    #展示转场效果
    for j in range(fps):
        weight = j/fps
        img = cv2.addWeighted(img1, 1-weight, img2, weight, 0)
        videoWrite.write(img)
for wait in range(fps):
    videoWrite.write(imglist[-1])

#提取视频帧并添加入视频
ret, frame = video.read()
while ret :
    cv2.putText(frame, text, textPos, cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 200, 200), 2)
    videoWrite.write(frame)
    ret, frame = video.read()
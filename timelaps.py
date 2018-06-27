#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import time

cnt = 1

def main():
    first = 0
    fourcc = cv2.VideoWriter_fourcc('I','Y','U','V')
    video = cv2.VideoWriter("data/timelaps.avi",fourcc,20.0,(640,480))

    print("Please set lap time:")
    laptime = input()
    laptime = int(laptime)
    
    global cnt

    while True:
        cnt = int(cnt)
        if first > 1:
            time.sleep(laptime)

            ret, frame = cap.read()
            if ret:
                cv2.imwrite("data/image"+str(cnt)+".png",frame)
                cnt += 1
        else:
            first = 1
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("data/image"+str(cnt)+".png",frame)
                cnt += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        for i in range(1,20):
            img = cv2.imread("data/image"+str(cnt)+".png",format(i))
            img = cv2.resize(img,(640,480))
            video.write(img)
        video.release()

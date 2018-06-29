#!/usr/bin/env python
# -*-coding: utf-8 -*-

import cv2
import time

cnt = 1
cap = cv2.VideoCapture(0)

print("Please set lap time:")
laptime = input()
laptime = int(laptime)

print("Please set flamerate:")
fps = input()
fps = int(fps)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter("data/timelaps.avi",fourcc,fps,(640,480))

def main():
    first = 0
    
    global cnt
    while True:
        cnt = int(cnt)
        if first == 1:
            time.sleep(laptime)
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("data/image"+str(cnt)+".jpg",frame)
                cnt += 1
        else:
            first = 1
            ret, frame = cap.read()
            if ret:
                cv2.imwrite("data/image"+str(cnt)+".jpg",frame)
                cnt += 1

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        mai = 1
        for i in range(1,cnt):
            img = cv2.imread("data/image"+str(mai)+".jpg")
            #img = cv2.resize(img,(640,480))
            video.write(img)
            mai += 1
        print("done")
        video.release()
        cv2.destroyAllWindows()

#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import time

def main():
    cap=cv2.VideoCapture(0)
    while(True):
        ret, frame=cap.read()
        detector = cv2.AKAZE_create()
        keypoints=detector.detect(frame)
        out=cv2.drawKeypoints(frame,keypoints,None,color=(0,0,255))
        if ret:
            cv2.imshow('keypoints',out)
        else:
            time.sleep(2)

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

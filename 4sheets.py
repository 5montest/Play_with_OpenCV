#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import numpy as np
import time

def main():
    cap=cv2.VideoCapture(0)
    while(True):
        ret, frame=cap.read()
        im_v=cv2.vconcat([frame,frame])
        im_h=cv2.hconcat([im_v,im_v])
        if ret:
            cv2.imshow('frame',im_h)
        else:
            time.sleep(2)

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

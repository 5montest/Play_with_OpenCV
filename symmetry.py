#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import numpy as np
import time

def main():
    cap=cv2.VideoCapture(0)
    while(True):
        ret, frame=cap.read()
        mirror=cv2.flip(frame,1)
        im_h=cv2.hconcat([frame,mirror])
        if ret:
            cv2.imshow('mirror',im_h)
        else:
            time.sleep(2)

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

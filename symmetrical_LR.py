#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import numpy as np
import time

def main():
    cap=cv2.VideoCapture(0)
    while(True):
        ret, frame=cap.read()
        mirror_u=cv2.flip(frame,1)
        im_h=cv2.hconcat([frame,mirror_u])
        mirror_d=cv2.flip(im_h,0)
        im_v=cv2.vconcat([im_h,mirror_d])
        if ret:
            cv2.imshow('2xmirror',im_v)
        else:
            time.sleep(2)

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

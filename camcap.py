#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import time

def main():
    cap=cv2.VideoCapture(0)
    while(True):
        ret, frame=cap.read()
        if ret:
            cv2.imshow('frame',frame)
        else:
            time.sleep(2)

        if cv2.waitKey(20) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

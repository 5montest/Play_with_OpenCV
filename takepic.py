#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import time

from datetime import datetime

def main():
    cap=cv2.VideoCapture(0)
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print(1)
    time.sleep(1)

    ret, frame=cap.read()
    if ret:
        cv2.imwrite(datetime.now().strftime("data/%Y-%m-%d-%H:%M:%S")+".png",frame)
if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*-coding: utf-8 -*-

import cv2
import numpy as np

def main():
    cap[0]=cv2.VideoCapture(0)
    cap[1]=cv2.VideoCapture(1)

    images = []
    while(True):
        for i in cap:
            ret, image = cap.read()
        if ret:
            frames.append(image)

            stitcher = cv2.createStitcher(True)
            stitched = stitcher.stitch(frames)
            cv2.imshow('panorama',stitched)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

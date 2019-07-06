"""
display the contents of the webcam with sift keypoints shown using OpenCV 
via the new Pythonic cv2 interface. The performance on this is pretty poor as expected, but should give an example of what's possible with opencv.
"""

import cv2
import numpy as np

def show_webcam(mirror=False):
    # The '0' argument for VideoCapture can be changed to match the index of the video device you wish to use.
    # ls -l /dev/ | grep video
    # this will give you a list of the video devices. Run this command before and after connecting USB webcam to determine index of camera
    # This index should correspond to the "/dev/videoX" argument index passed to the docker container.
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        sift = cv2.xfeatures2d.SIFT_create()
        kp = sift.detect(gray, None)
        image = cv2.drawKeypoints(gray,kp,img)
        cv2.imshow('my webcam', image)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

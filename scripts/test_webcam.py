"""
display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
"""

import cv2

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
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cv2.destroyAllWindows()


def main():
    show_webcam(mirror=True)


if __name__ == '__main__':
    main()

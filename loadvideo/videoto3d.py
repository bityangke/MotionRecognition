import numpy as np
import cv2

class Videoto3D:

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth  # depth is time axis(int)

    def video3d(self, filename):
        cap = cv2.VideoCapture(filename)
        nframe = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        frames = [x*nframe/self.depth for x in range(self.depth)]
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)

        for i in range(self.depth):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frames[i])
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite('file{}.png'.format(i), gray)



if __name__ == '__main__':
    vid = Videoto3D(120, 90, 10)
    vid.video3d('v_SkateBoarding_g25_c02.avi')

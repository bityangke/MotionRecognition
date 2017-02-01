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
        frames = [x * nframe / self.depth for x in range(self.depth)]
        #cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        #cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        gray = []

        for i in range(self.depth):
            cap.set(cv2.CAP_PROP_POS_FRAMES, frames[i])
            ret, frame = cap.read()
            frame = cv2.resize(frame, (self.height, self.width))
            gray.append(cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY))
            #cv2.imwrite('file{}.png'.format(i), gray[0])

        cap.release()
        return np.array(gray)

    def get_UCF_classname(self, filename):
        return filename[filename.find('_') + 1:filename.find('_', 2)]

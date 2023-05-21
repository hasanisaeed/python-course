import cv2


class Camera:

    def __init__(self, addr):
        self.capture = cv2.VideoCapture(addr)

    def get_frame(self):
        ret, frame = self.capture.read()
        return frame

    def draw_rect(self, point):
        ...  # pass


class Paint:
    pass

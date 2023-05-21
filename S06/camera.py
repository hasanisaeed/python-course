import cv2


class Camera:

    def __init__(self, addr):
        self.capture = cv2.VideoCapture(addr)

    def get_frame(self):
        # data = self.capture.read()
        # return data[1]

        ret, frame = self.capture.read()

        return frame
        # if ret:
        #     return frame
        # else:
        #     return None

cam = Camera("rtsp://admin:123456@192.168.1.120:554/stream1")  # 0

while True:
    frame = cam.get_frame()
    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

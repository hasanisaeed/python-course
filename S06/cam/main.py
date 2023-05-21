import cv2

from webcam import Camera
cam = Camera("rtsp://admin:123456@192.168.1.120:554/stream1")  # 0

while True:
    frame = cam.get_frame()
    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

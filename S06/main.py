import cv2

# اگه از وب کم لبتاتون استفاده میخواین کنین مقدار ورودی کلاس رو صفر بذارین

cam = cv2.VideoCapture("rtsp://admin:123456@192.168.1.120:554/stream1")

# data = cam.read()
# print(data)
#
# print('-------')
#
# print(type(data))

# frame = data[1]
# print(frame)

while True:
    data = cam.read()
    frame = data[1]

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

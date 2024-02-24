import cv2
import os

video = cv2.VideoCapture("oak-1110.mp4")

# extract images from video every 1 second
count = 0
name_video = "VID_20240217_113307"
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imwrite(os.path.join(f"./{name_video}", f"{name_video}_frame{count}.jpg"), frame)
    count += 1
    video.set(cv2.CAP_PROP_POS_MSEC, count * 1000)
    print(f"Frame {count} extracted")

video.release()
cv2.destroyAllWindows()
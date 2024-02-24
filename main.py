import cv2
import os

video = cv2.VideoCapture("oak-1110.mp4")

# extract images from video every 1 second
count = 0
while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break
    cv2.imwrite(os.path.join("./images", f"frame{count}.jpg"), frame)
    count += 1
    video.set(cv2.CAP_PROP_POS_MSEC, count * 1000)
    print(f"Frame {count} extracted")

video.release()
cv2.destroyAllWindows()
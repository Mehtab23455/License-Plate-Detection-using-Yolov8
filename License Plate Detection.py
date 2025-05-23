import cv2
import cvzone
import math
from ultralytics import YOLO



vid1 = r'C:\Users\Asus\Desktop\lpr-videos\5272112-uhd_3840_2160_30fps.mp4'
vid2 = r'C:\Users\Asus\Desktop\lpr-videos\6112061-hd_1920_1080_30fps.mp4'
vid3 = r'C:\Users\Asus\Desktop\lpr-videos\8321868-hd_1920_1080_30fps.mp4'
vid4 = r'C:\Users\Asus\Desktop\lpr-videos\11387586-hd_1920_1080_30fps.mp4'
vid5 = r'C:\Users\Asus\Desktop\lpr-videos\13654799_1920_1080_30fps.mp4'

cap = cv2.VideoCapture(vid3)

model = YOLO("C:/Users/Asus/Desktop/license-plate/numberplatemodel.pt")
classnames = ['license-plate','vehicle']

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1080,720))
    results = model(frame)


    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            confidence = box.conf[0]
            class_detect = box.cls[0]
            class_detect = int(class_detect)
            class_detect = classnames[class_detect]
            conf = math.ceil(confidence * 100)
            if conf > 50 and class_detect == 'license-plate':
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cvzone.putTextRect(frame, f'{class_detect}', [x1 + 8, y1 - 12], thickness=2, scale=1)



    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('t'):
        break

cap.release()
cv2.destroyAllWindows()
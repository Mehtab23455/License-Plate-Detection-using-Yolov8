import cv2
import cvzone
import math
from ultralytics import YOLO

# Load video
vid3 = r'C:\Users\Asus\Desktop\lpr-videos\8321868-hd_1920_1080_30fps.mp4'
cap = cv2.VideoCapture(vid3)

# Load YOLO model
model = YOLO("C:/Users/Asus/Desktop/license-plate/numberplatemodel.pt")
classnames = ['license-plate', 'vehicle']

while True:
    ret, frame = cap.read()
    if not ret:
        break  # End of video

    frame = cv2.resize(frame, (1080, 720))
    results = model(frame)

    for info in results:
        parameters = info.boxes
        for box in parameters:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            confidence = box.conf[0]
            class_detect = int(box.cls[0])
            label = classnames[class_detect]
            conf = math.ceil(confidence * 100)

            if conf > 50:
                color = (0, 255, 0) if label == 'license-plate' else (255, 0, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cvzone.putTextRect(frame, f'{label} {conf}%', [x1 + 8, y1 - 12], thickness=2, scale=1)

    # Show the frame
    cv2.imshow("YOLO Detection", frame)

    # Break if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


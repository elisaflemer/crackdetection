import cv2
from ultralytics import YOLO
import math

model = YOLO("best.pt")

img = cv2.imread("sample_pictures/rac.jpg")

results = model(img, stream=True)

for r in results:
        boxes = r.boxes

        for box in boxes:
            # bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

            # put box in cam
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # confidence
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # class name
            cls = int(box.cls[0])

            # object details
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, "rachadura: " + str(confidence), org, font, fontScale, color, thickness)

cv2.imshow('Webcam', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
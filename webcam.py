# Este script detecta rachaduras em em tempo real, usando a webcam do computador.

import cv2
from ultralytics import YOLO
import math

# carrega a webcam
cap = cv2.VideoCapture(0)

model = YOLO("best.pt")

# verifica se a webcam foi carregada corretamente
if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:

    # lê a imagem da webcam
    success, img = cap.read()

    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes

        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) 

            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            cls = int(box.cls[0])

            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            cv2.putText(img, "rachadura: " + str(confidence), org, font, fontScale, color, thickness)

    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
# Este script realiza a detecção de rachaduras em uma imagem

import cv2
from ultralytics import YOLO
import math

# carrega modelo treinado
model = YOLO("best.pt")

# carrega imagem
img = cv2.imread("sample_pictures/rac1.jpg")

# realiza a detecção
results = model(img, stream=True)

# adiciona as caixas delimitadoras na imagem e imprime a confiança da detecção
for r in results:
        boxes = r.boxes

        # desenha as caixas delimitadoras
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # calcula a confiança
            confidence = math.ceil((box.conf[0]*100))/100
            print("Confidence --->",confidence)

            # nome da classe (Rachadura)
            cls = int(box.cls[0])

            # detalhes do texto
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2

            # adiciona o texto na imagem
            cv2.putText(img, "rachadura: " + str(confidence), org, font, fontScale, color, thickness)

# mostra a imagem
cv2.imshow('Webcam', img)

# aguarda o usuário pressionar uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()
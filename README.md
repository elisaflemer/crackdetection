# Detecção de rachaduras com YoloV8

O projeto consiste na detecção de rachaduras usando o modelo YOLOv8, com base em um dataset fornecido pelo Roboflow. Para realizar o treinamento, foi utilizado o ambiente Colab, juntamente com um modelo pré-treinado do YOLO. O tutorial oficial da API em Python da versão 8 foi seguido para implementar o projeto.

Inicialmente, foi necessário baixar o dataset usando a chave API fornecida pelo Roboflow no Colab. Os dados foram salvos no runtime do Colab, seguindo a estrutura de pastas padrão do Roboflow, dentro de uma pasta chamada 'datasets'. Em seguida, o treinamento do modelo foi realizado por um determinado número de épocas, no caso, 10.

Então, o modelo foi exportado no formato ".pt" e carregado em dois arquivos Python. O primeiro arquivo, "picture.py", utiliza esse modelo para detectar rachaduras em imagens individuais, que devem estar armazenadas na pasta "sample_pictures". O segundo arquivo, chamado "webcam.py", permite a detecção de rachaduras em tempo real a partir da webcam do dispositivo. Ambos os scripts exibem um retângulo ao redor do objeto detectado, juntamente com a confiança da detecção. Para essa visualização, a biblioteca Python "opencv" é utilizada.

Dessa forma, o projeto combina a utilização do modelo YOLOv8 treinado com o dataset do Roboflow e as implementações dos scripts "picture.py" e "webcam.py" para realizar a detecção de rachaduras em imagens e em tempo real, respectivamente.

LINK DA DEMO: https://youtu.be/syQtT0MtCuw
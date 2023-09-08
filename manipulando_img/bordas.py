import cv2
import numpy as np

# Carregar e redimensiona a imagem
image_path = 'image/camaleao.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(0,0), fx=0.3, fy=0.3)

if image is not None:
    # Aplica o operador Canny para detecção de bordas
    edges = cv2.Canny(image, threshold1=100, threshold2=200)

    # Encontra os contornos na imagem
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Cria uma cópia da imagem original para desenhar os contornos
    image_with_contours = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # Desenha os contornos encontrados na imagem
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # Exibe as imagens em janelas separadas
    cv2.imshow('Imagem Original', image)
    cv2.waitKey(2000)
    cv2.imshow('Contornos Destacados', image_with_contours)
    cv2.waitKey(2000)
    cv2.imshow('Bordas Detectadas', edges)
    cv2.waitKey(2000)
    
    # Espera para fechar as janelas
    cv2.destroyAllWindows()
else:
    print('Erro ao carregar a imagem.')

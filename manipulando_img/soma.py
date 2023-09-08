import cv2

# Carregar e redimensiona a imagem em escala de cinza
image = cv2.imread('image/camaleao.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(0,0), fx=0.3, fy=0.3)

# Aplicar a limiarização (binarização)
threshold_value = 128  # Valor da limiar
max_value = 255       # Valor máximo para pixels acima da limiar
ret, binary_image = cv2.threshold(image, threshold_value, max_value, cv2.THRESH_BINARY)

# Detectar bordas
edges = cv2.Canny(image, 0, 255)

# Exibir a soma das imagens
cv2.imshow('Imagem Bordas', edges)
cv2.waitKey(2000)
cv2.imshow('Imagem Binaria', binary_image)
cv2.waitKey(2000)
cv2.imshow('Soma das imagens', edges + binary_image)
cv2.waitKey(2000)
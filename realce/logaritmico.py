import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem
imagem = cv2.imread('image/lena.jpg', 0)

# Processamento
c = 255 / np.log(1 + np.max(imagem))

imagem_realce_log = c * (np.log(imagem + 1))
imagem_realce_log = np.uint8(imagem_realce_log)

# Exibe a imagem original e a imagem realçada
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.title('Imagem Original')
plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Realce Logarítmico')
plt.imshow(imagem_realce_log, cmap='gray')
plt.axis('off')

plt.show()

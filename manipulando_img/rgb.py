import cv2
import numpy as np

# Carregar a imagem
imagem = cv2.imread('image/lena.jpg')

# Loop para alterar as cores
while True:
    # Exibe a imagem original
    cv2.imshow('Imagem Original', imagem)
    cv2.waitKey(1000) 

    # Copiar a imagem original
    imagem_vermelha = np.copy(imagem)
    imagem_verde = np.copy(imagem)
    imagem_azul = np.copy(imagem)

    # Alterar a cor para vermelho
    imagem_vermelha[:, :, 0] = 0  # Canal azul
    imagem_vermelha[:, :, 1] = 0  # Canal verde
    cv2.imshow('Imagem Vermelha', imagem_vermelha)
    cv2.waitKey(1000)

    # Alterar a cor para verde
    imagem_verde[:, :, 0] = 0  # Canal azul
    imagem_verde[:, :, 2] = 0  # Canal vermelho
    cv2.imshow('Imagem Verde', imagem_verde)
    cv2.waitKey(1000)

    # Alterar a cor para azul
    imagem_azul[:, :, 1] = 0  # Canal verde
    imagem_azul[:, :, 2] = 0  # Canal vermelho
    cv2.imshow('Imagem Azul', imagem_azul)
    cv2.waitKey(1000)

    # Sair do loop ao pressionar a tecla 'q'
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

# Fechar janelas
cv2.destroyAllWindows()

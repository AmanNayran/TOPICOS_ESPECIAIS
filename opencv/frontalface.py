import cv2

# Carrega a imagem a partir do arquivo
image = cv2.imread('image/criancas.jpg')
image = cv2.resize(image,(0,0), fx=0.2, fy=0.2)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

if image is not None:
    # Carrega o classificador pré-treinado para detecção de rostos
    algorithm = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

    # Detecta os rostos na imagem
    faces = algorithm.detectMultiScale(image_gray, scaleFactor=1.23, minNeighbors=3)

    # Imprime a matriz dos rostos detectados
    print(faces)

    # Desenha retângulos ao redor dos rostos detectados
    for(x, y, l, a) in faces:
        cv2.rectangle(image, (x, y), (x + l, y + a), (0, 255, 0), 2)

    # Exibe a imagem com os rostos detectados
    cv2.imshow("image", image)
    cv2.waitKey(1500)

else:
    print('Erro ao carregar a imagem.')


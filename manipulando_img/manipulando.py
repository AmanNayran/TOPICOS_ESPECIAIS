import cv2

# Carregar e redimensiona a imagem
image_path = 'image/camaleao.jpg'
image = cv2.imread(image_path)
image = cv2.resize(image,(0,0), fx=0.3, fy=0.3)

if image is not None:
    # Redimensiona a imagem para um novo tamanho
    new_size = (300, 200)
    resized_image = cv2.resize(image, new_size)

    # Converte a imagem para escala de cinza
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Aplica um filtro de desfoque
    blurred_image = cv2.GaussianBlur(image, (55, 55), 0)

    # Aplicar a limiarização (binarização)
    threshold_value = 128  # Valor da limiar
    max_value = 255       # Valor máximo para pixels acima da limiar
    ret, binary_image = cv2.threshold(gray_image, threshold_value, max_value, cv2.THRESH_BINARY)

    # Detectar bordas
    edges = cv2.Canny(image, 0, 255)


    # Exibe as imagens em janelas separadas
    cv2.imshow('Imagem Original', image)
    cv2.waitKey(2000)
    cv2.imshow('Imagem Redimensionada', resized_image)
    cv2.waitKey(2000)
    cv2.imshow('Imagem em Escala de Cinza', gray_image)
    cv2.waitKey(2000)
    cv2.imshow('Imagem Desfocada', blurred_image)
    cv2.waitKey(2000)
    cv2.imshow('Bordas', edges)
    cv2.waitKey(2000)
    cv2.imshow('Imagem Binarizada', binary_image)
    cv2.waitKey(2000)
    
    # Espera até que uma tecla seja pressionada e fecha as janelas
    cv2.destroyAllWindows()
else:
    print('Erro ao carregar a imagem.')

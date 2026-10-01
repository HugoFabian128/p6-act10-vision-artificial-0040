import numpy as np
import cv2
#Vision artificial Act 10NC = 0040
# Lee la imagen en escala de grises
img = cv2.imread("jupyter.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("jupyter 0040", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Linea
print(" La linea 0040")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)

# Abre la ventana con la imagen
cv2.imshow("line 0040", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# circulo
print(" el circulo 0040")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)

#  abrir el círculo
cv2.imshow("solo circulo 0040", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" el Texto 0040")
# Añade a la imagen el texto "Example Text" en color blanco
img = cv2.putText(img, "Hugo Fabaian 0040", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)

#  abrir el texto
cv2.imshow("solo texto 0040", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(" el Trackbars 0040")
def on_trackbar(val):
    pass

# 1. Crear ventana y lienzo de 520x520
cv2.namedWindow('frame')

# 2. Crear trackbars
cv2.createTrackbar('R', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('G', 'frame', 0, 255, on_trackbar)
cv2.createTrackbar('B', 'frame', 255, 255, on_trackbar)  # Inicia en azul

while True:
    # Validar que la ventana siga abierta antes de hacer nada
    if cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        break

    # Crear lienzo negro limpio en cada iteración
    img = np.zeros((520, 520, 3), np.uint8)

    # Leer trackbars de forma segura
    r = cv2.getTrackbarPos('R', 'frame')
    g = cv2.getTrackbarPos('G', 'frame')
    b = cv2.getTrackbarPos('B', 'frame')

    # Dibujar el círculo azul al centro (260, 260) con el color de los trackbars
    cv2.circle(img, (260, 260), 10, (b, g, r), -1)

    cv2.imshow('frame', img)

    # Salir con ESC (código 27)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

print(" el Thresholding 0040")
import cv2
import numpy as np

# 1. Cargar imagen en escala de grises (0)
img = cv2.imread('jupyter.jpg', 0)

# Validar que la imagen realmente se cargó
if img is None:
    print("Error: No se encontró 'image1.png'. Asegúrate de que esté en la misma carpeta.")
else:
    # 2. Aplicar los distintos tipos de umbralización
    ret, thr1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thr3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thr4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thr5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    # 3. Mostrar las 5 ventanas con las variantes
    cv2.imshow('BINARY', thr1)
    cv2.imshow('BINARY_INV', thr2)
    cv2.imshow('TRUNC', thr3)
    cv2.imshow('TOZERO', thr4)
    cv2.imshow('TOZERO_INV', thr5)

    # Esperar tecla para cerrar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

print("Hugo Fabian NC = 0040")
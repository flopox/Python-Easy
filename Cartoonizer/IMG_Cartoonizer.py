import cv2
import numpy as np

def cartoonize(image_path):
    # Leer la imagen
    image = cv2.imread(image_path)

    # Verificar si la imagen se cargó correctamente
    if image is None:
        print(f"No se pudo abrir o leer la imagen: {image_path}")
        return

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Ajustar los parámetros de umbral adaptativo para controlar la sensibilidad de los bordes
    edges = cv2.adaptiveThreshold(gray, 255,
                                  cv2.ADAPTIVE_THRESH_MEAN_C,
                                  cv2.THRESH_BINARY, blockSize=15, C=7)

    # Aplicar filtro bilateral para obtener colores suaves
    color = cv2.bilateralFilter(image, 9, 250, 250)

    # Crear la imagen tipo cartoon
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    # Mostrar la imagen original y la imagen cartoonizada
    cv2.imshow("Original Image", image)
    cv2.imshow("Cartoonized Image", cartoon)

    # Esperar a que se presione una tecla y luego cerrar las ventanas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Uso del cartoonizer con una imagen específica
cartoonize("C:/Path/de/la/imagen/a/cartoonizar/imagen.jpg") 
# ↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑ #
#Cualquier extensión de archivo relacionada a imagenes, es aceptada.

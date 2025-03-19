import cv2
import imutils

# HOG significa Histogram of Oriented Gradients, es un metodo de filtrado que calcula
# un vector para cada pixel de una imágen, que indica la dirección en la que la imágen
# se vuelve más obscura. Esto permite aproximar los bordes de las formas que hay en la
# propia imágen. Ciertos estudios han determinado que eqste metodo tiene un mejor
# rendimiento en la detección de personas a comparación de otros enfoques utilizados
# previamente. OpenCV cuenta con su propia implementación de este metodo, que será
# el que utilicemos para la detección de personas.
hog = cv2.HOGDescriptor()

# SVM significa Support Vector Machines, es el algoritmo de Machine Learning particular
# que se usa en conjunto con la información arrojada por el metodo HOG para determinar
# que formas dentro de la imágen deben categorizarse como personas.
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture('people_walk.mp4')

while cap.isOpened():
    # Es necesario analizar cada frame del video
    ret, image = cap.read()
    if ret:

        # Incrementar el tamaño del video aumenta la precisión del filtro,
        # pero requiere más recursos y se disminuye la fluidez con la que
        # se producen los resultados.
        videoSize = 400
        image = imutils.resize(image,
                               width=min(videoSize, image.shape[1]))

        # Detectar las regiones dentro de la imagen que tienen una persona
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(4, 4),
                                            padding=(32, 32),
                                            scale=1.05)

        # Mostrar numero de detecciones positivas
        print("Personas detectadas: " + str(len(regions)))

        # Dibujar los rectángulos de las regiones sobre la imágen
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                          (x + w, y + h),
                          (0, 0, 255), 2)

        # Mostrar las imágenes
        cv2.imshow("Image", image)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()
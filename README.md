# Semana_Tec_TC1001

El objetivo de este proyecto es utilizar herramientas de filtrado y visión computacional para extraer cierta utilidad de un grupo de imágenes.

Particularmente, optamos por desarrollar una funcionalidad de detección de personas en un video, el cual puede ser utilizado en múltiples casos como
análisis de videos de vigilancia o integrado como parte de las medidas de seguridad de un vehículo autónomo.

Utilizamos la librería de OpenCV ya que esta cuenta con un modelo pre entrenado para la detección de personas en imágenes.

Es necesario instalar esta librería para habilitar su funcionamiento: pip install opencv-python
También utilizamos la librería imutils para reescalar las imágenes extraídas del video, ya que es necesario reducir su tamaño para mejorar el 
rendimiento del proceso de análisis.


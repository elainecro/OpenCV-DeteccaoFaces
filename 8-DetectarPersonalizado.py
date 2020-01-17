# Para criar um classificador personalizado é necessário:
# - ter inúmeras imagens positivas
# - ter inúmeras imagens negativas
# - pode treinar com AdaBoost
# - o processamento pode ser muito demorado pois o algoritmo analisará pixel a pixel de toda a sua massa de imagens de treino
# - baixe os sources do opencv - https://opencv.org/releases/
# - uma ideia para separar as imagens negativas das positivas, é remover o objeto positivo da imagem e salva-la na lista das imagens negativas.
# - tenha muito mais imagens negativas do que positivas
# - tenha um arquivo de texto com o caminho das imagens
# - use opencv_createsamples - que retorna um arquivo .vec
# - use opencv_haartraining ou opencv_traincascade (mais eficiente)

# LINKS
# - https://github.com/andrewssobral/vehicle_detection_haarcascades
# - https://pythonprogramming.net/haar-cascade-object-detection-python-opencv-tutorial/
# - https://coding-robin.de/2013/07/22/train-your-own-opencv-haar-classifier.html
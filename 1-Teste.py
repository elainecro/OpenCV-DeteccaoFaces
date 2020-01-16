import cv2

print(cv2.__version__)

#Import image
imagem = cv2.imread('opencv-python-windows.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", imagem)
cv2.imshow("Tons de Cinza", imagemCinza)
cv2.waitKey()
import cv2
import matplotlib.pyplot as plt
import cvlib as cv

image_path = 'v1.jpg'
im=cv2.imread(image_path)
plt.imshow(im)
plt.show()

faces, confidences = cv.detect_face(im)

for face in faces:
    (startX, startY)=face[0], face[1]
    (endX, endY)=face[2], face[3]

    cv2.rectangle(im, (startX,startY), (endX,endY), (0,255,0), 2)

plt.imshow(im)
plt.show()
cv2.imwrite('result.jpg', im)

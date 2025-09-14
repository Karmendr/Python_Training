import cv2

img = cv2.imread('/home/runner/workspace/Karmendra_Deval/Images_code/dope-sukuna-pink-5120x2880-16935.png')
d = cv2.resize(img, (220, 220))
cv2.imwrite("resized.jpg",d)
# cv2.imshow("Resized image", d)

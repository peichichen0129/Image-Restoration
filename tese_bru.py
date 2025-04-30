import cv2
import numpy as np

img = cv2.imread('Test2_bru.jpg')
sharp_kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
after = cv2.filter2D(img, -1, sharp_kernel)
db = cv2.bilateralFilter(after,5,50,50)

cv2.imshow('repair.jpg', db)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('repair.jpg', db)
cv2.destroyAllWindows()

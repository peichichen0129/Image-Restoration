import numpy as np
import cv2
import scipy.special as special

def image_negative( f ):
	g = 255-2*f
	return g

def gamma_correction(f, gamma = 2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    c = 255.0/(255.0 ** gamma)
    table = np.zeros(256)
    for i in range(256):
        table[i] = round(i ** gamma * c, 0)
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]
    return g

def beta_correction(f, a = 2.0, b = 2.0):
    g = f.copy()
    nr, nc = f.shape[:2]
    x = np.linspace(0, 1, 256)
    table = np.round(special.betainc(a, b, x)*255, 0)
    if f.ndim != 3:
        for x in range(nr):
            for y in range(nc):
                g[x, y] = table[f[x, y]]
    else:
        for x in range(nr):
            for y in range(nc):
                for k in range(3):
                    g[x, y, k] = table[f[x, y, k]]
    return g

def main( ):
    img1 = cv2.imread( "Test_downtown1.jpg", -1 )
    #img2 = cv2.bitwise_not(img1)
    img3 = image_negative( img1 )
    img4 = gamma_correction(img3, 1.0)
    img5 = beta_correction(img4, a = 2.5, b = 2.5)
    cv2.imshow( "Original Image", img1 )
    cv2.imshow( "Image Negative", img5 )
    cv2.imwrite("Target.jpg", img5)
    cv2.waitKey( 0 )

main( )
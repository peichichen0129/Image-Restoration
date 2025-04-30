import numpy as np
import cv2

global img1,img2
filename = input("Enter filename:")
img1 = cv2.imread(filename,-1)
img2 = img1.copy()


def onMouse(event,x,y,flags,param):

    x,y=y,x
    print("(x,y)=(%d,%d)"%(x,y),end=" ")
    print("(R,G,B)=(%3d,%3d,%3d)"% (img1[x,y,2],img1[x,y,1],img1[x,y,0]))


def create_ROI():
    nr, nc = img2.shape[:2]

    ROI_LT = img2[279:380,6:58] 
    cv2.imwrite("LT.jpg",ROI_LT)
    ROI_MT = img2[420:506,172:288] 
    cv2.imwrite("MT.jpg",ROI_MT)
    ROI_RT = img2[446:503,331:447] 
    cv2.imwrite("RT.jpg",ROI_RT)
    ROI_SIGN = img2[145:191,204:355]  
    cv2.imwrite("SIGN.jpg",ROI_SIGN) 

def create_mask():
    nr, nc = img2.shape[:2]
    mask0=np.ones(img2.shape,dtype='uint8')
    mask1=mask0.copy()
    mask2=mask0.copy()
    mask3=mask0.copy()
    
    img_LT=cv2.imread("LT.jpg",1)
    nr_LT,nc_LT = img_LT.shape[:2]
    img_MT=cv2.imread("MT.jpg",1)
    nr_MT,nc_MT = img_MT.shape[:2]
    img_RT=cv2.imread("RT.jpg",1)
    nr_RT,nc_RT = img_RT.shape[:2]
    img_SIGN=cv2.imread("SIGN.jpg",1)
    nr_SIGN,nc_SIGN = img_SIGN.shape[:2]
    
    #flip image
    f_LT=cv2.flip(img_LT,-1)
    f_MT=cv2.flip(img_MT,-1)
    f_RT=cv2.flip(img_RT,-1)
    f_SIGN=cv2.flip(img_SIGN,-1)
    
    #mask
    mask0=f_LT[0:nr_LT,0:nc_LT]
    mask1=f_MT[0:nr_MT,0:nc_MT]
    mask2=f_RT[0:nr_RT,0:nc_RT]
    mask3=f_SIGN[0:nr_SIGN,0:nc_SIGN]
    
    img2[279:380,6:58] = mask0
    img2[420:506,172:288]  = mask1
    img2[446:503,331:447] = mask2
    img2[145:191,204:355] = mask3
    
def main():
    create_ROI()
    create_mask()
    cv2.namedWindow(filename)
    cv2.setMouseCallback(filename,onMouse) 
    cv2.imshow(filename, img1)
    cv2.imshow("Target", img2)
    cv2.imwrite("Target.jpg", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()
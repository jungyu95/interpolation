import cv2 as cv
import numpy as np
import lanczos

img = cv.imread('Lena.png')
#print(type(img[:,0,0]))
rows,colums,ch = img.shape

ch_temp=np.uint8(np.zeros([250,500,3]))

for i in range(rows):
    ch_temp[i,:,0] = lanczos.lanczos(img[i,:,0],500,1)    
    ch_temp[i,:,1] = lanczos.lanczos(img[i,:,1],500,1)    
    ch_temp[i,:,2] = lanczos.lanczos(img[i,:,2],500,1)    

ch_main=np.uint8(np.zeros([500,500,3]))

for i in range(500):
    ch_main[:,i,0] = lanczos.lanczos(ch_temp[:,i,0],500,4)    
    ch_main[:,i,1] = lanczos.lanczos(ch_temp[:,i,1],500,4)    
    ch_main[:,i,2] = lanczos.lanczos(ch_temp[:,i,2],500,4)    

test = cv.resize(img,(500,500),interpolation=cv.INTER_LANCZOS4)
cv.imshow("orginal",img)
cv.imshow("lanczos",ch_main)
cv.imshow("opencv",test)
cv.waitKey(0)
cv.destroyAllWindows()
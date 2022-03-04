import cv2 as cv
import numpy as np
import lanczos

order = 4
rsize_x = 1000
rsize_y = 500

img = cv.imread('Lena.png')
rows,colums,ch = img.shape


ch_temp=np.uint8(np.zeros([rows,rsize_x,3]))

for i in range(rows):
    ch_temp[i,:,0] = lanczos.lanczos(img[i,:,0],rsize_x,order)    
    ch_temp[i,:,1] = lanczos.lanczos(img[i,:,1],rsize_x,order)    
    ch_temp[i,:,2] = lanczos.lanczos(img[i,:,2],rsize_x,order)    


ch_main=np.uint8(np.zeros([rsize_y,rsize_x,3]))

for i in range(rsize_x):
    ch_main[:,i,0] = lanczos.lanczos(ch_temp[:,i,0],rsize_y,order)    
    ch_main[:,i,1] = lanczos.lanczos(ch_temp[:,i,1],rsize_y,order)    
    ch_main[:,i,2] = lanczos.lanczos(ch_temp[:,i,2],rsize_y,order)    

test = cv.resize(img,(rsize_x,rsize_y),interpolation=cv.INTER_LANCZOS4)
cv.imwrite("lee.png",ch_main)
cv.imwrite("opencv.png",test)
cv.imshow("orginal",img)
cv.imshow("lanczos",ch_main)
cv.imshow("opencv",test)
cv.waitKey(0)
cv.destroyAllWindows()
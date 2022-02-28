#Lanczos interpolation 
from cv2 import resize
import numpy as np
import math
import matplotlib.pyplot as plt

def kernel(x,order):
    #return value dtype is 1x1 ndarray
    pi_value = math.pi
    
    if x==0:
        weight_value=1
    elif x>=-order and x<=order:
        weight_value = (order*np.sinc(pi_value*x)*np.sinc([pi_value*x/order]))/(pi_value*x)**2
    else:
        weight_value=0
    return weight_value
    
    
def interpolation(x,points_value,order):
    #points dtype is ndarray 1xn
    #return value dtype is 1x1 ndarray
    x_floor=math.floor(x)
    interpolation_value = 0
    
    for i in range(x_floor-order+1, x_floor+order):
        try:
            interpolation_value += points_value[0,i]*kernel(x-i,order)
        except:
            interpolation_value += 0
    return interpolation_value

def data_resize(data,resize):
    new_data = np.zeros([1,resize])
    area = resize//data.size
    area_empty = resize%data.size 
    
    if area_empty == 0:
        for i in range(data.size):
            new_data[0,i*area] = data[0,i] 
    elif area_empty%2 == 0:
        for i in range(data.size):
            new_data[0,int(i*area+area_empty/2)] = data[0,i]

    else:
        for i in range(math.ceil(data.size/2)):
            new_data[0,i*area+area_empty//2] = data[0,i]
        for i in range(math.ceil(-data.size/2),-1):
            print(i) 
    return new_data
        

def lanczos(data,resize,order):
    #data mean : intensity
    resize_data = data_resize(data,resize)
    print(resize_data)
    interpolation_data=np.zeros([1,resize])
    for i in range(resize):
        interpolation_data[0,i] = np.uint8(interpolation((data.size/resize)*i,data,order))
    return interpolation_data

         
        

    
    

test_points = np.array([[1,2,3,4,5,6,7,8]])
new_points = np.array([[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]])
test_value = np.array([[240, 12, 120, 40, 80,70,100,255]])
new_value = lanczos(test_value,16,4)
test_value = data_resize(test_value,16)
print(new_value)
plt.scatter(new_points,test_value,20,'b')
plt.scatter(new_points,new_value,20,'r')
plt.show()
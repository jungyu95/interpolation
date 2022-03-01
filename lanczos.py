#Lanczos interpolation 
from cv2 import resize
import numpy as np
import math
import matplotlib.pyplot as plt

def kernel(x,order):
    #return value dtype is 1x1 ndarray
    pi_value = math.pi
    x=np.uint8(x)
   
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
            interpolation_value += points_value[i]*kernel(x-i,order)
        except:
            interpolation_value += 0
    return np.uint8(interpolation_value)

def data_resize(data,resize):
    new_data = np.zeros([resize])
    area = resize//data.size
    area_empty = resize%data.size 
    
    if area_empty == 0:
        for i in range(data.size):
            new_data[i*area] = data[i] 
    elif area_empty%2 == 0:
        for i in range(data.size):
            new_data[int(i*area+area_empty/2)] = data[i]

    else:
        for i in range(math.ceil(data.size/2)):
            new_data[i*area+area_empty//2] = data[i]
        for i in range(math.ceil(-data.size/2),-1):
            print(i) 
    return new_data
        

def lanczos(data,resize,order):
    #data mean : intensity
    resize_data = data_resize(data,resize)
    interpolation_data=np.zeros([resize])
    for i in range(resize):
        interpolation_data[i] = np.uint8(interpolation((data.size/resize)*i,data,order))
    return interpolation_data

         
        

    
    
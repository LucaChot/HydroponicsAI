import random
import math

#function to calculate growth depending on light
def light_growth(I):
    p = 0
    a = 0.004547 #variables declared by paper on activity of chloroplasts depending on light
    b = 0.9901
    c = 4.064
    print(I)
    #this was the equation of cholorplast activity to light intensity
    p = I/(a*(I^2) + b*I + c)
    print(p)

#function to calculate energy lost by convection 
def convec_calc():
    water_temp = int(input("Enter Water temp"))
    air_temp = int(input("Enter air temp"))
    dT = water_temp - air_temp
    hc = 3000
    A = int(input("Enter surface area within plant"))
    q = hc*A*dT
    print(q)

def temp_growth(T):
    R = math.sqrt(0.89)
    T_max = 37.1
    T_opt = 24.6
    R_max = 0.19
    R  = R_max * ((T_max - T)/(T_max - T_opt)) * (T/T_opt)
    print(R,T)


def start_grow():
    height = 0
    temp = 20
    light = 0

    return height, temp, light


        

def main():
    for i in range (0,35):
        temp_growth(i)


main()



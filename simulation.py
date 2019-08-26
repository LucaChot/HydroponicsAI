import random
import matplotlib.pyplot as plt 

def graph():

#function to calculate growth depending on light
def light_growth():
    p = 0
    a = 0.004547 #variables declared by paper on activity of chloroplasts depending on light
    b = 0.9901
    c = 4.064
    I = random.randint(0,100)
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


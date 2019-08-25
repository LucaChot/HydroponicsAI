import random
import matplotlib.pyplot as plt 

def graph():
    
def growth():
    p = 0
    a = 0.004547
    b = 0.9901
    c = 4.064
    I = random.randint(0,100)
    print(I)
    p = I/(a*(I^2) + b*I + c)
    print(p)

for i in range (1, 100):
    growth()

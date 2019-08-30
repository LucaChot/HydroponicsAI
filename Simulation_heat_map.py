
import matplotlib.pyplot as plt
import numpy as np

class Environment():

    # constructor function
    
    def __init__(self, water, air):

        self.water = water    # water temperature
        self.air = air        # air temperature

        self.dt = water - air  #temperature difference between water and air
    



class Plant():

    # set up constants for use in chloroplast activity

    A = 0.004547
    B = 0.9901
    C = 4.064


    # set up constants for temperature based activity

    TEMP_MAX = 37.1  #max temp 
    TEMP_OPT = 24.6  #optimum temp

    RATE_MAX = 0.19  #greatest rate
    

    Instances = []


    # constructor function - define parameters for specific object
    
    def __init__(self, light, temp, surface_area, environment):

        Plant.Instances.append(self)

        self.light = light
        self.temp = temp
        self.surface_area = surface_area
        self.environment = environment     # literal environment object
        
        self.growth_light = self.calculate_light()
        self.growth_temp = self.calculate_temp()
        self.loss_rate = self.calculate_loss()

        


    # returns energy gained via light

    def calculate_light(self):

        light = self.light
        growth = light / ((Plant.A * (light ** 2)) + (Plant.B * light) + Plant.C)

        return growth 


    # returns energy gained via temperature

    def calculate_temp(self):

        temp = self.temp
        #multiplied by 4 to ensure that light and heat had equal importance
        growth = (Plant.RATE_MAX * ((Plant.TEMP_MAX - temp)/(Plant.TEMP_MAX - Plant.TEMP_OPT)) * (temp / Plant.TEMP_OPT)) * 4

        return growth




    # return energy lost via convection

    def calculate_loss(self):

        environment = self.environment
        loss = self.surface_area * 3000 * environment.dt

        return loss



    # simple function - prints all calculations made for debugging
    
    def debug_calculation(self):

        print('\n\nplant gains: ', self.growth_light, ' via light')
        print('plant gains: ', self.growth_temp, ' via temperature')
        print('plant loses: ', self.loss_rate, ' via convection')

        print('\nplant overall gains/loses: ', self.growth_light + self.growth_temp)
        print('\The temperature dropped by: ', self.loss_rate)



Garden = Environment(30, 29.5)

#range of surrounding stimuli
temps = [0, 37.1 ,0.1]
lights = [0,801,1]

surface_area = 0.5

#list for heat map
Energy_Levels = []


#this loop creates the rows of the heat map

#runs throught each possible temperature
#changes the floats into integers
for temp in range(int((temps[1]-temps[0])//temps[2])):

    #each temperature has its own row
    row = []  

    #changes the floats into integers
    for light in range(int((lights[1]-lights[0])//lights[2])):
        
        #returns original value 
        plant_temp = temp * temps[2] + temps[0]
        plant_light = light * lights[2] + lights[0]
        
        #enters detail into classes to create an object
        a = Plant(plant_light, plant_temp, surface_area, Garden)
        
        #calculates total growth from light and temperature function
        row.append(a.growth_light + a.growth_temp)

    
    Energy_Levels.append(row)

#this makes the graph neater
fig, ax = plt.subplots()

#this creates a heat map, the brighter the area, the greater the rate of growth in that situation
plt.imshow(Energy_Levels, cmap='hot', interpolation='nearest')
#this flips the y axis
plt.gca().invert_yaxis()
#labels
plt.xlabel('Light Intensity (W/m^2)')
plt.ylabel('Temperature (°C)')
plt.title('Growth rate depending on light and temperature')

#this was to make sure that temperature was between 0 and 37 rather than measuring the instances
fig.canvas.draw()
labels = [item.get_text() for item in ax.get_yticklabels()]
labels = list(map(int, labels[1:]))
print(labels)

newlabels = [0]
for i in labels:
    i = i/10
    newlabels.append(i)

#replaces the tick labels
ax.set_yticklabels(newlabels)
plt.show()



#---------------------------------------------------------
# JASAMRIT RAHALA copyright
#----------------------------------------------------------
        

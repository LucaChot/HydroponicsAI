
import matplotlib.pyplot as plt


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

    TEMP_MAX = 37.1  #max temp for best growth
    TEMP_OPT = 24.6

    RATE_MAX = 0.19
    

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
        growth = (Plant.RATE_MAX * ((Plant.TEMP_MAX - temp)/(Plant.TEMP_MAX - Plant.TEMP_OPT)) * (temp / Plant.TEMP_OPT)) * 5

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

##'''
##myPlant = Plant(35, 35, 0.05, Garden)
##myPlant.debug_calculation()
##
##
##
##
##def remove_float(list_):
##    newlist_= []
##
##    multiplier = 1/list_[2]
##    print(multiplier)
##    for thing in list_:
##        print(thing)
##        thing = thing * multiplier
##        newlist_.append(int(thing))
##    print(newlist_)
##    return newlist_, int(multiplier)
##
##
##    
##
##
##def array_(temp, light): 
##    for temperature in range(temp[0][0], temp[0][1]):
##        temperature = temperature / temp[1]
##        for level in range(light[0][0], light[0][1]):
##            level = level/ light[1]
##            print(temperature,level)
##
##temp = [20,30,0.5]
##light = [50,70,1]
##
##
##temp = remove_float(temp)
##light = remove_float(light)
##
##array_(temp, light)
##
##
##'''



temps = [1, 37,0.1]
lights = [0,800,1]

surface_area = 0.5


Energy_Levels = []





for temp in range(int((temps[1]-temps[0])//temps[2])):

    row = []  

    
    for light in range(int((lights[1]-lights[0])//lights[2])):

        plant_temp = temp * temps[2] + temps[0]
        plant_light = light * lights[2] + lights[0]
        a = Plant(plant_light, plant_temp, surface_area, Garden)
        

        row.append(a.growth_light + a.growth_temp) #a.loss_rate)

    Energy_Levels.append(row)



'''

for plant in Plant.Instances:
    Energ_Levels.append(plant.growth_temp + plant.growth_light)
    print('Temp: ', plant.temp,' Light: ', plant.light, ' Growth: ', plant.growth_light+plant.growth_temp)


a = [[12,3,12],[1,34,34],[34,12,3]]

'''

plt.imshow(Energy_Levels, cmap='hot', interpolation='nearest')
plt.gca().invert_yaxis()
plt.xlabel('Light Intensity')
plt.ylabel('Temperature')
plt.title('Growth rate depending on light and temperature')
plt.show()



#---------------------------------------------------------
# JASAMRIT RAHALA copyright
#----------------------------------------------------------
        

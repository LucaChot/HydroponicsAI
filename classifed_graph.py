class Plant():

    RATE = 5

    # put all the constants here 
    # refer to the constants by calling Plant.[variable name]

    def __init__(self, var):
        self.var = var
        self.losses = []


    def __conv_loss__(self):

        self.var += 1
        return self.var / Plant.RATE



results = []
plants = []

for var in range(100):
    plants.append(Plant(var))


for plant in plants:

    for sweep in range(10):
        lossed = plant.__conv_loss__()
        plant.losses.append(lossed)


    results.append(plant.losses)


print(results)

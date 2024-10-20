
class MyCar: 

    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        
    def list_info(self): 
        print('This is a %s, that was made %d' % (self.brand, self.year))


# Creating new instance of car
first_car = MyCar('Toyota', 2002)

# Calling function
first_car.list_info()
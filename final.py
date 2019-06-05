

#from module import fun/class/variable
#from cars import car,cars_obj1
from automobile.cars.cars import * #--> Importing everythong from cars module
from automobile.bikes import bikes #--> importing bikes module from bikes sub package
if __name__ == "__main__":
    mycar = car("Benz")
    cars_obj1.print_name()
    print(version)
    print(bikes.version)
    print(__name__)
    print("Done...")


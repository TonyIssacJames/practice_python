
version = "1.2"
print("...importing.. ", __name__, " module")
class car:
    def __init__(self, name):
        self.name = name
        print("Initing car class is done")

    def print_name(self):
        print(self.name)

def create_car(name):
    car1 = car(name)
    return car1

def description():
    print("Module : cars, which has classes function cars at one place")

cars_obj1 = car("BMW")

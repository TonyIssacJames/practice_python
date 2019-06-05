'''

Bikes: It has classe, funcs, variables related to bikes...

'''
version = "1.2"
print("...importing.. ", __name__, " module")
class bike:
    def __init__(self, name):
        self.name = name
        print("Initing bike class is done")

    def print_name(self):
        print(self.name)

def create_bike(name):
    bike1 = bike(name)
    return bike1

def description():
    print("Module : bikes, which has classes function bikes at one place")

bikes_obj1 = bike("BMW")

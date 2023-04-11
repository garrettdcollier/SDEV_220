###########################
# Garrett Collier
# SDEV 220
# M03 Lab
# 4/10/23
#########################

# super class
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


# automobile class
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):

        # calls the super class
        Vehicle.__init__(self, vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # returns data to desired format
    def __str__(self):
        return "Vehicle type: " + self.vehicle_type + "\nYear: " + self.year + "\nMake: " + self.make + "\nModel: " + self.model + "\nNumber of doors: " + self.doors + "\nType of roof: " + self.roof


if __name__ == "__main__":
    # gets year, make, model, doors and roof information from the user
    year = input("Enter year: ")
    make = input("Enter make: ")
    model = input("Enter model: ")
    doors = input("Enter number of doors: ")
    roof = input("Enter type of roof: ")

    # creates an object of Vehicle type as car
    car = Automobile("car", year, make, model, doors, roof)
    # print details
    print("Entered details are: ")
    print(car)
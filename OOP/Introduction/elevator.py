class Elevator:
    def __init__(self, starting_floor):
        self.make = "Elevator Company"
        self.floor = starting_floor


# To create the object

elevator = Elevator(1)
print(elevator.make) # "The Elevator company"
print(elevator.floor) # 1
from enum import Enum

class Garage:

    def __init__(self):
        self._stock = []
    
    def add_tire(self, tire):
        if tire.needs_replacement():
            raise RuntimeError("This tire is already too worn out")
        else:
            self._stock.append(tire)

    def service_vehicle(self, vehicle):
        tires_replaced = 0

        while vehicle.has_worn_tires():
            new_tire = self._stock.pop()
            vehicle.replace_tire(new_tire)
            tires_replaced = tires_replaced + 1
        return tires_replaced


class FuelType(Enum):
    PETROL = 1
    DIESEL = 2

class FuelStation:

    def __init__(self):
        self._fuel = {}
    
    def has_fuel(self, fuel_type):
        return self._fuel.get(fuel_type, 0) > 0

    def _retrieve(self, fuel_type, amount):
        if self.has_fuel(fuel_type):
            amount_stored = self._fuel[fuel_type]
            if amount_stored - amount < 0:
                raise RuntimeError("Not enough fuel in station")
            else:
                self._fuel[fuel_type] = amount_stored - amount
        else:
            raise RuntimeError("No fuel of this type")

    def add_fuel(self, fuel_type, amount):
        if amount <= 0:
            raise ValueError("You can only add fuel and not take it")

        stored_amount = self._fuel.get(fuel_type, 0)
        self._fuel[fuel_type] = stored_amount + amount
    
    def fill_tank(self, fuel_type, vehicle):
        if vehicle.needs_fuel():
            fuel_needed = vehicle.amount_needed()
            self._retrieve(fuel_type, fuel_needed)
            vehicle.add_fuel(fuel_type, fuel_needed)
        else:
            raise RuntimeError("This vehicle has a full tank")
    
class Door:

    def __init__(self):
        self._is_closed = True
    
    def open(self):
        if self.is_closed():
            self._is_closed = False
        else:
            raise RuntimeError("Door is already open")

    def is_open(self):
        return not self._is_closed

    def close(self):
        if self.is_open():
            self._is_closed = True
        else:
            raise RuntimeError("Door is already closed")

    def is_closed(self):
        return self._is_closed

class Tire:

    def __init__(self, wear_level=46000):
        if wear_level <= 0:
            raise ValueError("Wear level must be a positive value")
        self._wear_level = wear_level
    
    def distance_before_worn(self):
        return self._wear_level
    
    def is_worn_out(self):
        return self._wear_level <= 0
    
    def needs_replacement(self):
        return self._wear_level < 500

    def will_be_worn_out(self, distance):
        return self._wear_level - distance < 0

    def register_wear(self, distance):
        if distance < 1:
            raise ValueError("Your can't travel negative distances")
        elif self.will_be_worn_out(distance):
            raise RuntimeError("Tire blown!")
        else:
            self._wear_level = self._wear_level - distance

class Engine:

    def __init__(self, fuel_type, capacity):
        self.fuel_type = fuel_type
        self._fuel_amount = 0
        self._fuel_capacity = capacity

    def add_fuel(self, type, amount):
        if type is not self.fuel_type:
            raise RuntimeError("This engine does not take this type of fuel")
        elif amount <= 0:
            raise ValueError("You cannot remove fuel from the engine")
        elif (amount + self._fuel_amount) > self._fuel_capacity:
            raise RuntimeError("This engine cannot hold this amount of fuel")
        else:
            self._fuel_amount = self._fuel_amount + amount
    
    def amount_needed(self):
        return self._fuel_capacity - self._fuel_amount
    
    def can_drive(self, distance):
        return self._fuel_amount - distance > 0

    def drive(self, distance):
        if self.can_drive(distance):
            self._fuel_amount = self._fuel_amount - distance
        else:
            raise RuntimeError("Not enough fuel to drive this distance")

class Vehicle:

    def __init__(self, tire_count, fuel_type, fuel_cap):
        self._engine = Engine(fuel_type, fuel_cap)
        self._tires = []
        
        if tire_count < 1:
            raise ValueError("A Vehicle must at least have 1 tire")

        for count in range(tire_count):
            self._tires.append(Tire())

    def has_worn_tires(self):
        for tire in self._tires:
            if tire.needs_replacement():
                return True
        return False
    
    def repace_tire(self, new_tire):
        tire_index = 0
        while tire_index < len(self._tires):
            if self._tires[tire_index].needs_replacement():
                self._tires[tire_index] = new_tire
                return
            tire_index = tire_index + 1
        raise RuntimeError("Found no tire which need replacement")

    def get_fuel_type(self):
        return self._engine.fuel_type

    def add_fuel(self, type, amount):
        self._engine.add_fuel(type, amount)
    
    def needs_fuel(self):
        return self._engine.amount_needed() > 0

    def amount_needed(self):
        return self._engine.amount_needed()
    
    def drive(self, distance):
        if not self._engine.can_drive(distance):
            raise RuntimeError("Cannot drive this distance: not enough fuel")
        
        for tire in self._tires:
            if tire.will_be_worn_out(distance):
                raise RuntimeError("Cannot drive this distance: tire will blow out")

        self._engine.drive(distance)
        for tire in self._tires:
            tire.register_wear(distance)

class Car(Vehicle):

    def __init__(
        self,
        fuel_type, 
        fuel_cap, 
        door_count
    ):
        super().__init__(4, fuel_type, fuel_cap)
        self.doors = []
        if door_count < 2:
            raise ValueError("A Car must at least have 2 doors")

        for count in range(door_count):
            self.doors.append(Door())
    
    def open_door(self, index):
        self.doors[index].open()
    
    def close_door(self, index):
        self.doors[index].close()
    
    def close_all_doors(self):
        for door in self.doors:
            if door.is_open():
                door.close()
    
    def has_open_doors(self):
        for door in self.doors:
            if door.is_open():
                return True
        return False

    def drive(self, distance):
        if self.has_open_doors():
            raise RuntimeError("Cannot drive with open doors")
        else:
            super().drive(distance)

class Motorcycle(Vehicle):

    def __init__(self, fuel_cap):
        super().__init__(2, FuelType.PETROL, fuel_cap)
    
    def do_wheely(self):
        raise RuntimeError("The Motorcycle has crashed!")

def main():
    station = FuelStation()
    station.add_fuel(FuelType.DIESEL, 100000)
    station.add_fuel(FuelType.PETROL, 100000)

    garage = Garage()
    for index in range(100):
        new_tire = Tire()
        garage.add_tire(new_tire)
    
    my_car = Car(FuelType.DIESEL, 800, 5)
    my_motor = Motorcycle(400)

    station.fill_tank(FuelType.DIESEL, my_car)
    print("I have filled the tank op my car. Ready to drive!")
    my_car.drive(355)
    print("I have driven a distance of 355 with my car")
    station.fill_tank(FuelType.PETROL, my_motor)
    print("I have filled the tank op my motorcycle. Ready to drive!")
    my_motor.drive(50)
    print("I have driven a distance of 50 with my motorcycle")
    try:
        station.fill_tank(FuelType.PETROL, my_car)
        print("I filled the tank of my car")
    except RuntimeError as error:
        print("Oops, I made a mistake: {}".format(error))
    
    print("I took my car to the garage for service")
    tires_replaced = garage.service_vehicle(my_car)
    print("They replaced {} of my tires".format(tires_replaced))

if __name__ == "__main__":
    main()



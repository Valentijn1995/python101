from parts import Engine, Tire, Door
from fuel import FuelType

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

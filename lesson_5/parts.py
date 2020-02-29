
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
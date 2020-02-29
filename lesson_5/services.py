

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
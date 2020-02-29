from services import FuelStation, Garage
from fuel import FuelType
from vehicles import Car, Motorcycle
from parts import Tire

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

# Classes

Classes allow you to group a set of variables and function together. The functions
in the class can be used to change the global variables in the class. Global
class variables can be accessed within the functions be using the **this** keyword.

```Python

class Counter:

    def __init__(self, initial_count):
        self._count = initial_count
    
    def increase(self):
        self._count = self._count + 1

    def decrease(self):
        self._count = self._count - 1
    
    def __len__(self):
        return self._count

```

## An example

Lets take a look at an example. We want to create a program where we can make two types of vehicles:
a car and a motorcycle. We want to be able to take our vehicle to the tank station to fill up the tank.
We also want to be able to take our vehicle to the garage where they will replace the tires if they are
to worn off.

Lets break apart the story above:

* We have a Vehicle 
  * A vehicle can be a car
    * A car has doors
  * A vehicle can be a motorcycle
  * A vehicle has an engine
    * An engine needs fuel to operate
  * A vehicle needs tires to be able to move
    * Tires can get worn out
* The fuel tank of a vehicle can be filled at a fuelstation
  * A fuelstation can offer different types of fuel
* Worn tires can be replaced at a garage

De next thing we are going to do is to create an UML. UML stands for Unified Modeling Language.
An UML can be used to create a high level blueprint of our future Python program. You will
need a separate piece of software to create an UML diagram. I recommend 
[Voilet UML](http://alexdp.free.fr/violetumleditor/page.php) but you are free to use whichever
program you like.

Our first model will look like [this](classes_uml.class.violet.html). This model clearly shows
the connections between the different classes. The Motorcycle and Car classes are two types
of vehicle and a vehicle need Tires and an Engine to function. The car class also needs
doors. De Garage and Fuelstation class work with the vehicle class.
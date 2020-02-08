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

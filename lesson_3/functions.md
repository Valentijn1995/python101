# Functions
You sometimes have pieces of code which you need multiple times (often with small variations).
It is often wise to put these pieces of code in a function.

A function has the following structure:

```Python
def my_function(argument1, argument2):
    # Function logic
    result = argument1 + argument2
    return result
```

The function starts of with a name. It can optionally also have one or more arguments.
The arguments are input for the function. The results of the function are given back
to the function caller by using the **return** statement. All variables which are
declared in the function can only be used within the function.

The following example demonstrates how to use the function:

```Python
def my_function(argument1, argument2):
    # Function logic
    result = argument1 + argument2
    return result

first_number = 5
second_number = 10

sum = my_function(first_number, second_number)
print("The sum of {} and {} is {}".format(first_number, second_number, sum))
```



# Lines starting with a # are comments. These lines are ignored by Python.


# It is recommended to give your variables proper names.

# This variable holds a string. A string is simply a piece of text and
# is defined between single of double quotes.
street_name = "John Street"

# This variable holds an integer.
street_number = 61

# This variable holds a Boolean value which can be either True or False
has_doorbell = False

# The following line of code shows a line of text on the output console.
# Try changing the value of the variables above and observe
# the changes to the console output.

print("John lives on {} number {} and has {} doorbell".format(
        street_name, 
        street_number, 
        "yes" if has_doorbell else "no" 
    )
)

# Python also has lists. A list is a collection of separate pieces of data and can be defined by using brackets.
my_shopping_list = ["apple", "milk", "cookies", "toilet paper"]

# The following code writes the shopping list as output to the console.
# Try adding and removing items from the list as see how the output changes.
print("My shopping list:")
for item in my_shopping_list:
    print("- {}".format(item))

# You can access the individual items in the list like this:
first_item_on_list = my_shopping_list[0]
print("The first item on my list is {}".format(first_item_on_list))

# Note that lists start at the number zero and not one.

# Python also has a data type called a dictionary. A dictionary contains a
# set of unique keys which are mapped to values. It can be compared to
# a real word dictionary. The dictionary contains words (the keys) and
# each word is mapped to a definition.
#
# Dictionaries can be created with braces.
my_shopping_list = {"apple": 6, "milk": 1, "cookies": 20, "toilet paper": 3}

# The following code writes the shopping list as output to the console.
# Try adding and removing items from the list as see how the output changes.
print("My improved shopping list:")
for item, quantity in my_shopping_list.items():
    print("- {}: {}".format(item, quantity))

# You can access a specific value in the dictionary by using it's key:
amount_of_apples = my_shopping_list["apple"]
print("I have to get {} apples from the shop".format(amount_of_apples))

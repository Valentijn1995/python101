import json
import sys
import os
from enum import Enum

ROOT_NAME = "shopping_list"

class Action(Enum):
    ADD = 1
    DELETE = 2
    SAVE = 3
    QUIT = 4


def print_list(list):
    if len(list) == 0:
        print("Your shopping list is empty")
    else:
        print("Shopping list:")
        counter = 1
        for item in list:
            print("{}. {} ({})".format(counter, item["name"], item["quantity"]))
            counter = counter + 1

def ask_for_action():
    print("These are your options:")
    print("[1] Add an item")
    print("[2] Delete an item")
    print("[3] Save list")
    print("[4] Quit")
    answer = input("What would you like to do?:")
    action = Action(int(answer))
    return action

def load(path):
    global ROOT_NAME
    with open(path, 'r') as input_file:
        data = json.load(input_file)
        return data[ROOT_NAME]

def try_load(path):
    try:
        return load(path)
    except FileNotFoundError:
        return []

def save(path, shopping_list):
    global ROOT_NAME
    data = {ROOT_NAME: shopping_list}
    with open(path, 'w') as out_file:
        json.dump(data, out_file, indent=4)

def main():
    file_name = "shopping_list.json"
    shopping_list = try_load(file_name)

    while True:
        print_list(shopping_list)
        print("")
        action = ask_for_action()

        if action is Action.ADD:
            name = input("Item name: ")
            if len(name) == 0:
                print("Error: The name cannot be empty")
            else:
                quantity_str = input("Quantity: ")
                try:
                    quantity = int(quantity_str)
                    shopping_list.append({"name": name, "quantity": quantity})
                except ValueError:
                    print("Error: Quantity must be a number")

        elif action is Action.DELETE:
            item_number_str = input("What item number would you like to delete:")
            try:
                item_number = int(item_number_str)
                index = item_number - 1
                del shopping_list[index]
            except ValueError:
                print("Error: please supply a number")
            except IndexError:
                print("Error: no item with this number")
        elif action is Action.QUIT:
            print("Good bye!")
            sys.exit()
        elif action is Action.SAVE:
            print("Saving list...")
            save(file_name, shopping_list)
            print("Shopping list saved as {}".format(file_name))

if __name__ == "__main__":
    main()
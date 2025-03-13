"""Create a program that simulates a shopping list.
The program must:
1. Prompt the user to add items to the shopping list.
    - Continue prompting until the user types "exit".
    - Do not allow duplicate items in the list.
2. Display the final shopping list sorted in alphabetical order.
3. Prompt the user to remove items from the list, if desired.
    - Continue prompting until the user types "exit".
    - Display the updated list after each removal."""


class ShoppingList:

    def __init__(self):
        # docstring
        self.shopping_list = []

    def add_item(self, item):
        # docstring
        if item in self.shopping_list:
            print("Item already added!")
        else:
            self.shopping_list.append(item)

    def sort_list(self):
        # docstring
        self.shopping_list.sort()
        self.display_list()

    def remove_item(self, item):
        # docstring
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed!")
            self.display_list()
        else:
            print("This item is not in the list.")

    def display_list(self):
        print("Your shopping list:")
        for item in self.shopping_list:
            print(item.title())


my_list = ShoppingList()

while True:
    item = (
        input("Add an item to the shopping list (or type 'exit' to view the list): ")
        .strip()
        .lower()
    )
    if item == "exit":
        break
    if not item.strip():
        print("Invalid item! Please enter a valid item.")
        continue
    my_list.add_item(item)

my_list.sort_list()

while True:
    item = (
        input(
            "Would you like to remove an item? Type the item name (or 'exit' to finish the program): "
        )
        .strip()
        .lower()
    )
    if item == "exit":
        print("Program finished. See you later!")
        break
    my_list.remove_item(item)

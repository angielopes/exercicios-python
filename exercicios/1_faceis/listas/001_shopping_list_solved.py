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
    """
    A class to represent a shopping list.

    Attributes
    ----------
    shopping_list : list
        a list to store shopping items

    Methods
    -------
    add_item(item):
        Adds an item to the shopping list if it is not already present.
    sort_list():
        Sorts the shopping list in alphabetical order and displays it.
    remove_item(item):
        Removes an item from the shopping list if it is present.
    display_list():
        Displays the current shopping list.
    """

    def __init__(self):
        """
        Initializes a new instance of the shopping list.
        This constructor initializes an empty shopping list.
        """
        
        self.shopping_list = []

    def add_item(self, item):
        """
        Adds an item to the shopping list.
        Args:
            item (str): The item to be added to the shopping list.
        Returns:
            None
        Prints a message if the item is already in the shopping list.
        """
        
        if item in self.shopping_list:
            print("Item already added!")
        else:
            self.shopping_list.append(item)

    def sort_list(self):
        """
        Sorts the shopping list in alphabetical order and displays the sorted list.
        This method sorts the items in the `shopping_list` attribute in place using
        the default sorting order (alphabetical). After sorting, it calls the 
        `display_list` method to show the sorted list to the user.
        """
        
        self.shopping_list.sort()
        self.display_list()

    def remove_item(self, item):
        """
        Removes an item from the shopping list.
        Parameters:
            item (str): The item to be removed from the shopping list.
        Returns:
            None
        If the item is found in the shopping list, it is removed and a message 
        "Item removed!" is printed, followed by the updated shopping list. 
        If the item is not found, a message "This item is not in the list." is printed.
        """
        if item in self.shopping_list:
            self.shopping_list.remove(item)
            print("Item removed!")
            self.display_list()
        else:
            print("This item is not in the list.")

    def display_list(self):
        """
        Displays the shopping list.
        This method prints each item in the shopping list with the first letter
        of each word capitalized.
        """

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

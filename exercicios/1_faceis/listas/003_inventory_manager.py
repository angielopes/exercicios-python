"""Create a program that manages the inventory of a store. The program must allow:
1. Adding products to the inventory with:
    - Product name.
    - Initial quantity of the product.
2. Removing products from the inventory:
    - The user must provide the product name and the quantity to be removed.
    - If the quantity to be removed is greater than the available quantity, display an error message
    and ask for another input.
3. Display the updated inventory:
    - After each addition or removal operation, show the list of products and their quantities.
*  Bonus challenge:
    - Do not allow products with the same name to be added to the inventory.
    If this happens, only update the quantity.
"""

from utils import confirm_action, get_valid_int, get_valid_string


class Product:
    """
    A class used to represent a Product.

    Attributes
    ----------
    name : str
        The name of the product.
    quantity : int
        The quantity of the product in stock.

    Methods
    -------
    __init__(name, quantity)
        Initializes the Product with a name and quantity.
    """

    def __init__(self, name, quantity):
        """
        Initialize an InventoryManager object.
        Parameters:
            name (str): The name of the item.
            quantity (int): The quantity of the item in inventory.
        """
        self.name = name
        self.quantity = quantity


class Inventory:
    """
    A class to manage an inventory of products.

    Attributes
    ----------
    products : list
        A list to store the products in the inventory.

    Methods
    -------
    add_product(product_name, quantity):
        Adds a specified quantity of a product to the inventory.
        If the product already exists, it updates the quantity.
    remove_product(product_name, quantity):
        Removes a specified quantity of a product from the inventory.
        If the quantity reaches zero, the product is removed from the inventory.
    display_inventory():
        Displays the current inventory with product names and their quantities.
    """

    def __init__(self):
        """
        Initializes the InventoryManager with an empty list of products.
        """
        self.products = []

    def add_product(self, product_name, quantity):
        """
        Adds a product to the inventory. If the product already exists, it updates the quantity.
        Args:
            product_name (str): The name of the product to add or update.
            quantity (int): The quantity of the product to add.
        Returns:
            None
        """
        # Check if the product already exists in the inventory
        for product in self.products:
            if product.name == product_name:
                product.quantity += quantity
                print(f"{quantity} units added to the product {product_name}.")
                return

        new_product = Product(product_name, quantity)
        self.products.append(new_product)
        print(f"{quantity} units added to the new product {product_name}.")

    def remove_product(self, product_name, quantity):
        """
        Removes a specified quantity of a product from the inventory.
        Args:
            product_name (str): The name of the product to be removed.
            quantity (int): The quantity of the product to be removed.
        Returns:
            None
        Prints:
            A message indicating the quantity removed and the product name.
            A message indicating if the product is out of stock and removed from the inventory.
            A message indicating insufficient quantity in inventory if the requested quantity is more than available.
            A message indicating the product is not found if the product does not exist in the inventory.
        """
        for product in self.products:
            if product.name == product_name:
                if product.quantity >= quantity:  # Check if there is enough quantity
                    product.quantity -= quantity
                    print(f"{quantity} removed from the product {product_name}")

                    # If the quantity reaches zero, remove the product from inventory
                    if product.quantity == 0:
                        self.products.remove(product)
                        print(
                            f"Product {product_name} is out of stock and removed from the inventory."
                        )
                    return
                else:
                    print("Insufficient quantity in inventory!")
                return

        print("Product not found.")

    def display_inventory(self):
        """
        Display the current inventory of products.
        This method prints the name and quantity of each product in the inventory.
        If the inventory is empty, it notifies the user that the inventory is empty.
        """
        # Display inventory after each iteration
        if self.products:
            print("\nCurrent inventory:")
            for product in self.products:
                print(f"{product.name}: {product.quantity} units.")
        else:
            print("Inventory is empty.")


# Run program

my_inventory = Inventory()

while True:
    # Inventory menu
    print(
        """\nOPTIONS:
            [1] Add product
            [2] Remove product
            [3] View inventory
            [4] Exit
            """
    )

    option = get_valid_int("Choose an option: ", min_value=1, max_value=4)

    # Exit the program
    if option == 4:
        if confirm_action("Are you sure you want to exit?"):
            print("Program finished...")
            break

    # Add products
    elif option == 1:
        product = get_valid_string("Product name: ")
        initial_qty = get_valid_int("Quantity to be added: ", min_value=1)
        my_inventory.add_product(product, initial_qty)
        my_inventory.display_inventory()

    # Remove products
    elif option == 2:
        remove_product = get_valid_string("Product name: ")
        remove_qty = get_valid_int("Quantity to be removed: ", min_value=1)
        my_inventory.remove_product(remove_product, remove_qty)
        my_inventory.display_inventory()

    # Display inventory
    elif option == 3:
        my_inventory.display_inventory()

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

inventory = []

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
    try:
        option = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Exit the program
    if option == 4:
        print("Program finished...")
        break

    # Add products
    elif option == 1:
        product = input("Product name: ").capitalize()
        initial_qty = int(input("Quantity to be added: "))

        # Check if the product already exists in the inventory
        for item in inventory:
            if item[0] == product:
                item[1] += initial_qty
                print(f"{initial_qty} units added to the product {product}")
                break
        else:
            inventory.append([product, initial_qty])
            print(f"{initial_qty} units added to the new product {product}")

    # Remove products
    elif option == 2:
        remove_product = input("Product name: ").capitalize()
        remove_qty = int(input("Quantity to be removed: "))

        for item in inventory:
            if item[0] == remove_product:
                if item[1] >= remove_qty:  # Check if there is enough quantity
                    item[1] -= remove_qty
                    print(f"{remove_qty} removed from the product {remove_product}")
                    if item[1] == 0:
                        inventory.remove(item)
                        print(
                            f"Product {remove_product} is out of stock and removed from the inventory."
                        )
                else:
                    print("Insufficient quantity in inventory!")
                break
        else:
            print("Product not found.")

    # Show inventory
    elif option == 3:
        print("\nDisplaying full inventory...")
    else:
        print("Invalid option. Try again.")

    # Display inventory after each iteration
    if inventory:
        print("\nCurrent inventory:")
        for item in inventory:
            print(f"{item[0]}: {item[1]} units")
    else:
        print("Inventory is empty.")

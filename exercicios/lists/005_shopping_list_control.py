"""Create a program to manage a shopping list.
Each item will have a product name, its quantity, and the unit price. The program should allow:
1. Adding a product to the shopping list.
2. Removing a product from the list.
3. Calculating the total purchase value.
4. Displaying all items with the name, quantity, and total price of each product."""

shopping_list = []

while True:
    print(
        """
            Options:
    [1] Add product
    [2] Remove product
    [3] View shopping list
    [4] Calculate total
    [5] Exit"""
    )

    try:
        option = int(input("\nChoose an option: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Exit the program
    if option == 5:
        print("Program closed...")
        break

    # Add products, quantity, and price
    elif option == 1:
        product = input("Product name: ").capitalize().strip()
        try:
            product_qty = int(input("Quantity: "))
            unit_price = float(input("Unit price: "))
        except ValueError:
            print("Quantity and price must be valid numbers.")
            continue

        # Check if the item already exists (if it exists, just add the quantity)
        for item in shopping_list:
            if item[0] == product:
                item[1] += product_qty
                print(
                    f"{product_qty} units added to the product {product} in the shopping list."
                )
                break
        else:
            shopping_list.append([product, product_qty, unit_price])

    # Remove products
    elif option == 2:
        remove_product = (
            input("Which product do you want to remove from the list? ")
            .capitalize()
            .strip()
        )
        for item in shopping_list:
            if item[0] == remove_product:
                shopping_list.remove(item)
                print(f"{remove_product} removed from the list.")
                break
        else:
            print(f"The product {remove_product} is not in the shopping list.")

    # View shopping list
    elif option == 3:
        if shopping_list:
            print("\nSHOPPING LIST:")
            for item in shopping_list:
                total_product_value = item[1] * item[2]
                print(
                    f"{item[0]} - Quantity: {item[1]} - Unit Price: $ {item[2]:.2f} - Total: $ {total_product_value:.2f}"
                )
        else:
            print("Shopping list is empty.")

    # Calculate total purchase value
    elif option == 4:
        if shopping_list:
            total_purchase_value = sum(item[1] * item[2] for item in shopping_list)
            print(f"\nTotal purchase value: $ {total_purchase_value}")
        else:
            print("Shopping list is empty.")

    else:
        print("Invalid option. Try again.")

"""It's the same as
    total_purchase_value = 0
    for item in shopping_list:
        total_purchase_value += item[1] * item[2]"""

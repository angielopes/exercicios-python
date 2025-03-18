def get_valid_int(prompt, min_value=None, max_value=None):
    """Prompts the user for an integer, ensuring it is valid and within a range."""
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Enter a number greater than or equal to {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Enter a number less than or equal to {max_value}.")
            else:
                return value
        except ValueError:
            print("Enter a valid integer.")


def get_valid_float(prompt, min_value=None, max_value=None):
    """Prompts the user for a decimal number (float), ensuring it is valid and within a range."""
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Enter a number greater than or equal to {min_value}.")
            elif max_value is not None and value > max_value:
                print(f"Enter a number less than or equal to {max_value}.")
            else:
                return value
        except ValueError:
            print("Enter a valid number.")


def get_valid_string(prompt, allowed_values=None):
    """Prompts the user for a string and optionally validates whether it is within an allowed set."""
    while True:
        value = input(prompt).strip().capitalize()
        if not value:
            print("Input cannot be empty. Try again.")
        elif allowed_values and value not in allowed_values:
            print(f"Invalid input. Allowed values: {', '.join(allowed_values)}")
        else:
            return value


def confirm_action(prompt):
    """Requests confirmation from the user (Y/N)."""
    while True:
        value = input(prompt + " (Y/N): ").strip().upper()
        if value in ["Y", "N"]:
            return value == "Y"
        else:
            print("Invalid input. Enter 'Y' for Yes or 'N' for No.")

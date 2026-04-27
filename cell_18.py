def check_integer():
    user_input = input("Enter an integer: ")
    try:
        if not user_input.lstrip('-').isdigit():
            raise ValueError(f"Invalid input: '{user_input}' is not a valid integer.")

        val = int(user_input)
        print("Valid integer entered:", val)

    except ValueError as e:
        print(e)

check_integer()
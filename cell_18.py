while True:
    try:
        num = int(input("Enter an integer: "))
        print(f"Valid integer entered: {num}")
        break
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
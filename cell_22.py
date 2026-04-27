def copy_file():
    src = input("Enter source filename: ")
    dst = input("Enter destination filename: ")

    try:
        with open(src, 'r') as f1, open(dst, 'w') as f2:
            for line in f1:
                f2.write(line)
        print(f"Successfully copied '{src}' to '{dst}'.")

    except FileNotFoundError:
        print(f"Error: The source file '{src}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

copy_file()
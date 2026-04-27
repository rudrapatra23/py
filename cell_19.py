def read_file():
    filename = input("Enter the filename to open: ")
    try:
        file = open(filename, 'r')
        content = file.read()
        print("File content:")
        print(content)
        file.close()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

read_file()
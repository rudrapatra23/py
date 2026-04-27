def access_list_element(data, index):
    try:
        result = data[index]
        print(f"Element at index {index}: {result}")
    except IndexError:
        print(f"Error: The index {index} is out of range for this list.")

my_list = [10, 20, 30, 40, 50]

access_list_element(my_list, 2)
access_list_element(my_list, 10)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):

        if self.is_empty():
            return "Stack is empty! Cannot pop."
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty!"
        return self.items[-1]

    def display(self):
        print(f"Current Stack (Bottom to Top): {self.items}")

my_stack = Stack()

while True:
    print("\n1. Push | 2. Pop | 3. Peek | 4. Display | 5. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        val = input("Enter value to push: ")
        my_stack.push(val)
    elif choice == '2':
        print(f"Popped element: {my_stack.pop()}")
    elif choice == '3':
        print(f"Top element: {my_stack.peek()}")
    elif choice == '4':
        my_stack.display()
    elif choice == '5':
        break
    else:
        print("Invalid choice, try again.")
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):

        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)


    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None or current_node.val == key:
            return current_node is not None
        if key > current_node.val:
            return self._search_recursive(current_node.right, key)
        return self._search_recursive(current_node.left, key)


bst = BinarySearchTree()

print("Binary Search Tree Operations")
nums = input("Enter numbers to insert separated by space: ").split()

for n in nums:
    bst.insert(int(n))

find_val = int(input("Enter a value to search for: "))
if bst.search(find_val):
    print(f"Found {find_val} in the tree!")
else:
    print(f"{find_val} does not exist in the tree.")
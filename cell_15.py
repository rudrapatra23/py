import math
class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

# Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Triangle
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


print("Choose a shape: 1. Circle 2. Square 3. Triangle")
choice = input("Enter choice (1/2/3): ")

if choice == '1':
    r = float(input("Enter radius: "))
    obj = Circle(r)
elif choice == '2':
    s = float(input("Enter side length: "))
    obj = Square(s)
elif choice == '3':
    a = float(input("Enter side A: "))
    b = float(input("Enter side B: "))
    c = float(input("Enter side C: "))
    obj = Triangle(a, b, c)
else:
    print("Invalid choice")
    exit()

print(f"\nArea: {obj.area():.2f}")
print(f"Perimeter: {obj.perimeter():.2f}")
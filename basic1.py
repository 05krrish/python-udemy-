name = input("Enter your name: ")

print("Hello, " + name + "!")   

##fundamental data types
print(type(2+4))
print(type(3.5))
print(type("Hello"))
print(type(True))
print(type(False))
print(type(None))
print(type([1, 2, 3]))
print(type((1, 2, 3)))
print(type({"key": "value"}))
print(type({1, 2, 3}))

#operators precedence
result = 3 + 4 * 2 / (1 - 5) ** 2 ** 3
print(result)

# order >> parentheses, exponentiation, multiplication/division, addition/subtraction
a = 10
b = 3       
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b
floor_division = a // b
modulus = a % b
exponentiation = a ** b
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Floor Division:", floor_division)
print("Modulus:", modulus)
print("Exponentiation:", exponentiation)

#variables and assignment
x = 5
y = 10
sum_xy = x + y
print("Sum of x and y:", sum_xy)
x, y = y, x
print("After swapping, x:", x)
print("After swapping, y:", y)
print("Value of pi:", 3.14159)
radius = 7
area = 3.14159 * radius ** 2
print("Area of the circle:", area)
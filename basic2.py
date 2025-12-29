
#type conversion
print(type(str(100)))
print(type(int("100")))
print(type(float("3.14")))
print(type(bool(1)))

#escape sequences
print("Hello\nWorld")
print("Hello\tWorld")
print("He said, \"Hello World!\"")
print('It\'s a beautiful day!')
print("C:\\Users\\Name")

#formatted strings
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
print("My name is {} and I am {} years old.".format(name, age))
# Variables
x = 15
print(x)

#string formatting
name = "Ram"
print(f"Hello, {name}")

greeting = "Hello, {}"
with_name = greeting.format(name)
print(with_name)

# User input
name = input("Enter your name:")
print(f"Hello you entered {name}")

# Lists, tuples
l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

print(f"First element in list is {l[0]}")
print ("Second element in tuple is {}".format(t[1]))
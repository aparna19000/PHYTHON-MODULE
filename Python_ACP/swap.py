#SWAPPING
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a, "b =", b, "c =", c)

temp = a
a = b
b = c
c = temp

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)




#SIMPLE WAY TO CODE
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
c = int(input("Enter third number (c): "))

print("\nBefore swapping:")
print("a =", a, "b =", b, "c =", c)

# Swapping
a, b, c = b, c, a

print("\nAfter swapping:")
print("a =", a, "b =", b, "c =", c)

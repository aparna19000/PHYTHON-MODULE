print("ASCII Value Checker")
print("-" * 30)

# Take input from user
char = input("Enter any single character: ")

# Check if user entered exactly 1 character
if len(char) != 1:
    print("Error: Please enter ONLY ONE character.")
else:
    ascii_value = ord(char)   # ord() gives ASCII value
    print(f"The ASCII value of '{char}' is: {ascii_value}")

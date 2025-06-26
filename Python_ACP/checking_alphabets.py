
print("Welcome, Radhika! Let's identify your character.")


user_input = input("Enter a single character: ")

# Check if the input is exactly one character long
if len(user_input) == 1:
    #.isalpha() method to check if the character is an alphabet a-z or A-Z
    if user_input.isalpha():
        print(f"'{user_input}' is an alphabet.")
    else:
        print(f"'{user_input}' is NOT an alphabet (it's a number, symbol, or space).")
else:
   
    print("Please enter only a single character.")

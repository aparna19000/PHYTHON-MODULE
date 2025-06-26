import math

user_input_str = input("Enter the number you want to find the square root of: ")

number = float(user_input_str)

if number >= 0:
  
    square_root = math.sqrt(number)

 
    print(f"The square root of {number} is: {square_root}")
else:
  
    print("Cannot calculate the square root of a negative number (in real numbers).")



MIN_TEMP = 18.0 
MAX_TEMP = 30.0  

print("Welcome, Rohan! Let's check the weather for your clothes.")


temp_input = input("Enter the current temperature in Celsius: ")
current_temperature = float(temp_input)


if MIN_TEMP <= current_temperature <= MAX_TEMP:
    print(f"It's {current_temperature}°C. Perfect! You can wear light and soft clothes today.")
elif current_temperature > MAX_TEMP:
    print(f"It's {current_temperature}°C. That's quite warm! You'll definitely be comfortable in light clothes.")
else:
    print(f"It's {current_temperature}°C. Hmm, it might be a bit too cold for only light clothes. Consider a jacket or pullover.")


#Task 2: Temperature Conversion
'''Create a Python program that converts temperatures between Celsius and Fahrenheit. 
Prompt the user to enter a temperature value and the unit of measurement, and then 
display the converted temperature.'''

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32
    
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def temperature_conversion():

    input_temp = input("enter the input:").upper().strip()
    
    try:
        if (input_temp.endswith("C")):
            c = input_temp.strip("C") #input: 37C
            result = celsius_to_fahrenheit(float(c))
            print(f"{c}°C is {result:.2f}°F") 
        elif (input_temp.endswith("F")):
            f = input_temp.strip("F") #input: 98.6F
            result = fahrenheit_to_celsius(float(f))
            print(f"{f}°F is {result:.2f}°C")
        else: #input: 37
            print("Invalid input, Use number followed by C or F (e.g., 98.6F, 37C).")
    except ValueError: #input: abdC or njfF
        print("Invalid input, Please enter a valid temperature.")
        
temperature_conversion()
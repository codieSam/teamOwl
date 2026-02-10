# In this exercise, you will write a Python program that allows the user to convert temperatures from Celsius to Fahrenheit and Kelvin. 

# Your Task is to look at the following requirements and implement the program in the file called temperature_converter.py.

# Requirements:
# -	The user stores the Celsius value as a number in a variable called celsius_input
# -	The Celsius value then gets converted to Fahrenheit and stored in a variable called degree_f
# -	The Celsius value then gets converted to Kelvin and stored in a variable called degree_k
# (Note: Use the internet to find out the formulas on how to convert C to K and F and implement that using Python operators
# -	Generate and print an output that follows the following format:

# Welcome to the Temperature Converter!

# The temperature you have entered is {USER ENTERED C} degree Celsius.

# Converted Temperatures:
# {USER ENTERED C} degree Celsius is equal to {COMPUTED degree_f} Fahrenheit.
# {USER ENTERED C} degree Celsius is equal to {COMPUTED degree_k} Kelvin.

# Thank you for using the Temperature Converter!



# Once you are finished with this task, please show the output of this and the code to your lab tutor for formative feedback. 

print("Hey user, Welcome to temperature converter !")
print("For C to F, type 0 & for F to C type 1")
input_value = int(input())
if(input_value == 0):
    print("Insert temp in Celcius: ")
    celsius_input = float(input())
    converted_temp = (celsius_input * 9/5) + 32
    print("The tempoerature in Forenhite is", (converted_temp), "F")
elif(input_value == 1):
    print("Insert temp in Forenhite: ")
    forenhite_input = float(input())
    converted_temp = (forenhite_input - 32) * 5/9


    print("The tempoerature in Forenhite is", (converted_temp), "Celcius")
else:
    print("Invalid input ! Please type 1 or 0 only.")




celsius_input = float(input())
converted_temp = (celsius_input * 9/5) + 32
print("The tempoerature in Forenhite is", (converted_temp), "Forenhite")
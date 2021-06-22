print("Welcome to the Temperature Conversion Program")

#Get user input
input_required = True
while input_required:
    try:
        temp_far = float(input("What is the temperature in degrees Fahrenheit: "))
        break
    except ValueError:
        print("That is not a valid temperature, please try again.")
        
#convert the temps and round

temp_celcius = (5/9) * (temp_far - 32)
temp_kelvin = temp_celcius + 273.15

temp_far = round(temp_far,4)
temp_celcius = round(temp_celcius,4)
temp_kelvin = round(temp_kelvin,4)

#print results

print("Degrees Fahrenheit:\t" + str(temp_far))
print("Degrees Celcius:\t" + str(temp_celcius))
print("Degrees Kelvin:\t" + str(temp_kelvin))
print("Welcome to the MPH to MPS Conversion App")

condition = True
while condition == True:
    try:
        mph_speed = float(input("What is your speed in MPH: "))
        break
    except ValueError:
        print("That is not a valid number, please try again using digits")
        
mph_speed = float(mph_speed)
meter_per_sec = mph_speed * 0.4474
meter_per_sec = round(meter_per_sec, 2)
print("Your speed in meters per second is " + str(meter_per_sec) + ".")
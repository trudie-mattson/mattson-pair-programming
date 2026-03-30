#Option 1. Takes two values (feet and inches) and converts to meters


#function
def meters(feet, inches):

    if feet.isalpha() == True or inches.isalpha() == True: #check for alpha values
        print('Please input a number for feet and inches')
        feet = input('feet: ')
        inches = input('inches: ')
        return meters(feet, inches)
    #do calculations
    feet_meters = float(feet) * 0.3048
    inches_meters = float(inches) * 0.0254
    value = feet_meters + inches_meters

    return value

print('Hello! this is a feet/inches to meter conversion')
#Ask for feet and inches input
feet = input('feet: ')
inches = input('inches: ')
#run function
print(f' your input was {feet} feet and {inches} inches. Your result is {meters(feet, inches)} meters.')
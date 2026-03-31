#Option 1. Takes two values (feet and inches) and converts to meters


#function
def meters(feet, inches):
    if feet.isalpha() == True or inches.isalpha() == True: #check for alpha values
        #this if statement doesnt work, it causes an error, I think the .isaplha() operator is not working.
        print('Please input a number for feet and inches')
        feet = input('feet: ')
        inches = input('inches: ')
        return meters(feet, inches)
    #do calculations
    feet_meters = float(feet) * 0.3048
    inches_meters = float(inches) * 0.0254
    value = feet_meters + inches_meters
#other then the .isalpha() operator the code looks good.
    return value

#Option 1. Takes two values (feet and inches) and converts to meters
#Option 4. Takes an input array and returns values scaled to lie in the range of 0.0 to 1.0


#BASELINE DOWN. ERRORS WHEN LETTER INPUTTED INSTEAD OF NUMBER

#Ask for feet an inches input
string = input("Hello! Welcome to the feet/inches to meters conversion. \n To start, please type a measurement in this form: 'feet inches' use numbers and type '0' if none for either.\n ex. '0 13' or '2 0' or '5.3 1' \n")


#split the string into a list: [feet, inches]
while ' ' not in string: #checks if format is mostly correct
    string = input("You must input a string in this format: 'feet inches' if you do not have feet, or do not have inches, please use a 0 to replace that value. \n ex. '0 2' or '2 0'. \n Please input a new string: ")
list = string.split()
#print(list)
#print(len(list))

while len(list) !=2: #checks if there are two values in correct format
    string = input("Your input must have exatly two values: 'feet inches' if you do not have feet, or do not have inches, please use a 0 to replace that value. \n ex: '0 2.3'or '2.5 0' \n Please input a new string: ")
    list = string.split()

#BREAKS HERE WHEN LETTER IS INPUTTED. While not working as intended.
while (float(list[0]) == False) or (float(list[1]) == False): #checks if values are numbers
    string = input("Your input must be numbers: 'feet inches' if you do not have feet, or do not have inches, please use a 0 to replace that value. \n ex: '0 2.3'or '2.5 0' \n Please input a new string: ")
    list = string.split()

#convert strings to floats
#assign variables to feet value and inches value
feet = float(list[0])
#print(f'feet:{feet}')
inches = float(list[1])
#print(f'inches:{inches}')

#compute conversion
feet_meters = feet * 0.3048
inches_meters = inches * 0.0254

#sum the feet component to inches component to get final value
meters = feet_meters + inches_meters

#result
print(f'\nFeet to meter conversion complete. \nInput: {feet} feet and {inches} inches. \nFinal result: {round(meters, 4)} meters')
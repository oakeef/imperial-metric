__author__ = 'w0174181'

#enter number in miles
miles = float(input("Enter the number of miles: "))
#enter number of yards
yards = float(input("Enter the number of yards: "))
#enter number of feet
feet = float(input("Enter the number of feet: "))
#enter number of inches
inches = float(input("Enter the number of inches: "))
#do math
#find total amount of inches
totalInches = (63360 * miles) + (36 * yards) + (12 * feet) + inches
#find total meters
totalMeters = totalInches / 39.37
#find total centimeters so it is easier to work with
totalCent = totalMeters*100
#find kilometres
kilometres = int(totalMeters / 1000)
#this is where I use the modulo expression to find the remainders
meters = int(totalMeters%1000)
cent = float(totalCent%100)

#this section is me printing the numbers to see what I was getting
#print(totalInches)
#print(totalMeters)
#print(totalCent)
#print(kilometres)
#print(kilometres, meters, round(cent, 1))

#list length in kms, metres, centimetres
print("The metric length is " + str(kilometres) + " kilometres, " + str(meters) + " metres, " + str(round(cent, 1)) + " centimetres")

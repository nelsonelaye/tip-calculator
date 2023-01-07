#In this project, I will create a simple calculator that determines the price of a meal after tax and tip.

# meal is $44.5
meal = 44.50

# tax is 6.75% 
# getting the decimal value for the tax
tax = 6.75/100

# tip is 15%
# getting the decimal value also
tip = 15/100

meal += meal*tax
total = meal + (meal*tip)

print("Total cost of meal is " + str(total))

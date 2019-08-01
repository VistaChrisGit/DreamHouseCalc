#Saving for a dream house

annualSalary = float(input('Enter your annual salary: '))
portionSaved = float(input('Enter the percent of your salary to save as a decimal: '))
totalCost = float(input('Enter the cost of your dream home: '))

portionDownPayment = totalCost * .25 #target we need to hit to place our down payment

currentSavings = 0 #state vaiable for how much we have saved
numberOfMonths = 0 #state variable for number of months passed

monthlySalary = annualSalary/12
monthlySavings = monthlySalary * portionSaved
investmentReturn = currentSavings*.04/12


while currentSavings <= portionDownPayment:
    investmentReturn = currentSavings*.04/12 #we are getting back 4% on our savings each year
    
    currentSavings += monthlySavings
    currentSavings += investmentReturn
    
##    print(currentSavings) #printing to help debug, make sure incrementing correctly
    
    numberOfMonths += 1
    

    
print('Number of months you need to save for:',numberOfMonths)

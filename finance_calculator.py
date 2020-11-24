import math
#Finacial calculator Python program
print ("investment\t- to calculate the amount of interest you'll earn on interest \nbond \t\t- to calculate the amount you'll have to pay on a home loan")

#user inputs their decision on which they would like to calculate
choice = input("Choose either 'investment' or 'bond' from the menu below to proceed: \n")

#elif statements for bond or investments
if choice == "investment" or choice == "INVESTMENT" or choice == "Investment":
    deposit = float(input("The amount you will be depositing: "))
    int_rate = int(input(" The interest rate: "))
    years = int(input("The number of years you plan on investing for.:"))
    interest = input ("Do you want 'compound' or 'simple' interest: ")
    #elif statements for simple and compound interest
    if interest == "simple" or interest == "Simple" or interest == "SIMPLE":
        sum = deposit * (1 + (int_rate/100) * years)
        print(sum)
    elif interest == "compound" or interest == "Compound" or interest == "COMPOUND":
        sum = deposit * math.pow(1 + (int_rate/100) , years)
        
    else:
        print (" You have not entered a valid input!")
        
elif choice == "bond" or choice == "BOND" or choice == "Bond":
    value = int(input("The value of the house: "))
    int_rate = (int(input("The interest rate: "))/12)
    months = int(input("Over how many months do you want to repay?: "))
    sum = (int_value * value) / (1 - math.pow((1 + int_value),(- month)))
    print (sum)


    
else:
    print (" You have not entered a valid input!")

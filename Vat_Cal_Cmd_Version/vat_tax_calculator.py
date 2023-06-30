import time #import time module

def get_percentage_input(): # Def function to Get percentage input from user, return valid percentage as float
    while True:
        try:
            percentage = float(input("Please enter Total Percentage of VAT Tax of your country: "))
            if percentage >= 0 and percentage <= 100: #Check if percentage is within range
                print(("\n***Percentage Total Entered:"), (percentage))
                return percentage
            else:
                print("\nPercentage must be between 0 and 100") #inform user of invalid input of percentage
        except ValueError:
            print("\nInvalid input, please enter a valid percentage\n") #inform user of invalid input

def get_amount(): #Def function to Get amount input from user, return valid amount as float
    while True:
        try:
            amount = float(input("Please enter an amount to calculate percentage on: "))
            if amount >= 0: #Check if amount is positive number
                print(("\n***Amount Entered:"), (amount), ("\n"))
                return amount

            else: #inform user of invalid input
                print("\nAmount must be a positive number\n")

        except ValueError: #inform user of invalid input
            print("\nInvalid input, please enter a valid amount\n")

def program(): #Main , executes program
        #Welcome and introduction to user with some instructions and information
        print("\nWelcome to the Simple Universal VALUE ADDED TAX/SALES TAX Calculator!")
        print("Please enter the required information when prompted.")
        time.sleep(1) #All timesleep functions in program are for readability and simulation of calculating/loading.
        print("To calculate the VAT/SALES TAX, enter the total VAT/SALES percentage of tax for your country.")
        print("If your country has multiple tax inputs on VAT and sales tax, combine those \npercentages and enter the full percentage.")
        print("To add or deduct the tax amount from an amount entered, enter + or - respectively.")
        print("\nLet's get started!\n")
        time.sleep(1)

        amount = get_amount() #Get input for amount
        percentage = get_percentage_input() #Get input for percentage

        tax_calculation = amount * percentage / 100.00 #Calulation of VAT Amount
        time.sleep(1)
        #Inform user of calculated Vat tax amount
        print("\n***The calculated VAT/SALES TAX amount on the entered amount is:", tax_calculation, "\n")

        while True: #Prompt user for instructions to continue or quit
            print("Enter '+' to add the VAT/SALES TAX to Amount")
            print("Enter '-' to deduct the VAT/SALES TAX from Amount")
            print("Enter 'quit' to exit")
            option_input = input(":")

            if option_input == "quit":
                time.sleep(1) #Thank user for using program
                print("\nThank you for using my Simple VAT/SALES TAX Calculator!")
                print("I hope you found this tool helpful.")
                time.sleep(1) #Request feedback
                print("If you have any feedback or suggestions for improvement, please let me know.")
                print("Thank you again for your support!")
                time.sleep(1) #Provide Author information
                print("Best regards, Rethar Osman Abdullah")
                print("https://github.com/Rethar-yt")
                break

            elif option_input == "+":
                result = amount + tax_calculation
                time.sleep(1) #Inform user of Inclusive amount
                print("\n***Total Amount Inclusive of VAT:", result, "\n")

            elif option_input == "-":
                result = amount / (1 + (percentage / 100.0))
                time.sleep(1) #Inform user of Exclusive amount
                print("\n***Total Amount Exclusive of VAT:", result, "\n")


            else:
                time.sleep(1) #Inform user of invalid input
                print("\nInvalid input detected. Please choose an option from the available options and try again.\n")

program()

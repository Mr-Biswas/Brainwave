
# Project Title: ATM Machine Program

import time
# Imported the time module to handle time-related functions

# Displayed initial message indicating that ATM is now operational and asking to insert a debit card
print("##################### ATM Machine on Action ################################# \n::::: Please Insert Your Debit Card & Wait :::::")

# Paused the program for 5 seconds to simulate time taken to insert the card
time.sleep(5)

# Predefined correct PIN for authentication
password = 1234

# Asked the user to enter their 4-digit PIN
pin = int(input("Enter Your 4-Digit PIN: "))

# Predefined account balance for the demonstration
balance = 11111

# Checked if the entered PIN matches the correct one
if pin == password:
    while True:
        # Displayed the menu with different options available for the user
        print("""
            1 == Check Balance
            2 == Withdraw Amount
            3 == Deposit Amount
            4 == Exit
    """)

        try:
            # Asked the user to choose an option and converting it to an integer
            option = int(input("\n:::::: Please Enter Your Choice::::::\n"))
        except:
            # In case of an invalid input (non-integer), printed a message asking for valid input
            print("Please Enter valid option:")

# Checked the user's choice and execute the corresponding block of code
        if option == 1:
            # Option 1: Check Balance
            print(f"Your current Account Balance is Rs.{balance}")
        # Option 2: Withdraw Amount
        if option == 2:
            # Display the current balance to inform the user of available funds for withdrawal
            print(
                f"::::::::::::::::::::::::::::::::::::::::::: Available Balance Rs.{balance}:::::::::::::::::::::::")

# Asked the user to input the withdrawal amount
            withdraw_amount = int(input("\nWithdrawal Amount: "))

# Subtracted the withdrawal amount from the balance and update the balance
            balance = balance - withdraw_amount

# Informed the user that the withdrawal was successful and show the remaining balance
            print(f"Please Collect Rs{withdraw_amount}.")
            print(
                f"Your current balance is Rs.{balance}.\n:::::::::::::::::::::::::::::::::: Thank You :::::::::::::::::::::::::::::::::::::")

        if option == 3:  # Option 3: Deposit Amount
            # Displayed the current balance to inform the user of available funds for deposit
            print(
                f"::::::::::::::::::::::::::::::::::::::::::: Available Balance Rs.{balance}:::::::::::::::::::::::")

# Asked the user to input the deposit amount
            deposit_amount = int(input("\nDeposit Amount: "))

# Added the deposit amount to the balance and updated the balance
            balance = balance + deposit_amount

# Informed the user that the deposit was successful and show the new balance
            print(f"Rs{deposit_amount} has been deposited.")
            print(
                f"Your current balance is Rs.{balance}.\n:::::::::::::::::::::::::::::::::: Thank You ::::::::::::::::::::::::::::::::::::::")

        if option == 4:  # Option 4: Exit
            # Printed a thank-you message and break the loop to exit the ATM system
            print("Thanks for choosing Us.\n--------------------------------- Visit Again --------------------------------------------------- ")
            break

else:
    # If the entered PIN is incorrect, display an error message and prompt for correct PIN
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ Please Enter correct PIN $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

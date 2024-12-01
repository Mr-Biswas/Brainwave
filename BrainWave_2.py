# Project Title: Bank Management System

# Imported MySQL connector to interact with the MySQL database
import mysql.connector

# Establishing connection to the MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password='123456',
    database='sbi_bank'
)

# Checked if the connection to the database is successful
if mydb.is_connected():
    print("Connection Established")

# Function to open a new account


def OpenAcc():
    n = input("Enter the Name: ")
    an = input("Enter the Account Number: ")
    db = input("Enter the Date of Birth: ")
    add = input("Enter the Address: ")
    cn = input("Enter the Contact Number: ")
    ei = input("Enter the Email: ")
    # Get opening balance (converted to integer)
    ob = int(input("Enter the Opening Balance: "))

    # Data to be inserted into the 'Accounts' and 'Amount' tables
    # Account details
    data1 = (n, an, db, add, cn, ei, ob)
    # Account name, account number, and opening balance for the 'Amount' table
    data2 = (n, an, ob)

    # SQL query to insert customer data into the 'Accounts' table
    sql1 = "INSERT INTO Accounts VALUES (%s, %s, %s, %s, %s, %s, %s)"
    # SQL query to insert account balance into the 'Amount' table
    sql2 = "INSERT INTO Amount VALUES(%s, %s, %s)"

    # Creating a cursor to execute SQL commands
    a = mydb.cursor()

    # Executing the SQL queries to insert data into both tables
    a.execute(sql1, data1)
    a.execute(sql2, data2)

    # Committing the changes to the database
    mydb.commit()

    print("Task Accomplished without Any Error.")  # Print success message
    main()
    # Called main() to display the menu again

# Function to deposit money into an account


def DepositMoney():
    # Get deposit amount (converted to integer)
    amount = int(input("Enter the amount to be deposited? "))
    # Get account number to identify the account
    an = input("Enter the Account Number: ")

    # SQL query to fetch current balance for the given account number
    b = 'SELECT Balance FROM Amount WHERE AccNo=%s'
    data = (an,)
    # Tuple containing account number
    a = mydb.cursor()

    # Execute the query to get the current balance for the given account number
    a.execute(b, data)
    result = a.fetchone()
    # Fetch the result from the database

    # Calculate the new balance after depositing the money
    bal = result[0] + amount

    # SQL query to update the balance in the 'Amount' table
    sql = 'UPDATE Amount SET Balance=%s WHERE AccNo=%s'
    c = (bal, an)
    # Tuple containing new balance and account number
    a.execute(sql, c)

    # Commit the changes to the database
    mydb.commit()

    print("Task Accomplished without Any Error.")
    main()
    # Call main() to display the menu again

# Function to withdraw money from an account


def WithdrawMoney():
    # Get withdrawal amount (converted to integer)
    amount = int(input("Enter the amount to withdraw? "))
    an = input("Enter the Account Number: ")  # Get account number

    # SQL query to fetch current balance for the given account number
    b = 'SELECT Balance FROM Amount WHERE AccNo=%s'
    data = (an,)
    # Tuple containing account number
    a = mydb.cursor()

    # Execute the query to get the current balance for the given account number
    a.execute(b, data)
    result = a.fetchone()
    # Fetch the result from the database

    # Calculate the new balance after withdrawing the money
    bal = result[0] - amount

    # SQL query to update the balance in the 'Amount' table
    sql = 'UPDATE Amount SET Balance=%s WHERE AccNo=%s'
    c = (bal, an)
    # Tuple containing new balance and account number
    a.execute(sql, c)

    # Commit the changes to the database
    mydb.commit()

    print("Task Accomplished without Any Error.")
    main()

# Function to check the balance of an account


def Balance():
    an = input('Enter the Account Number: ')

# SQL query to fetch details of the account
    d = 'SELECT * FROM Amount WHERE AccNo=%s'

# Create a cursor object to execute the query
    a = mydb.cursor()
    data = (an, )

# Executed the query to get account balance
    a.execute(d, data)
    result = a.fetchall()
    # Fetch the result from the database

# Displayed the balance
    if result:

        print()
        print("Balance for Account Number", an, "is", result[-1])
        main()
        # Call main() to display the menu again
    else:
        # Error message for invalid account number
        print("Invalid Input")
        main()

# Function to display customer details


def CustomerDetails():
    an = input('Enter the Account Number: ')

# SQL query to fetch customer details from the 'Accounts' table
    d = 'SELECT * FROM Accounts WHERE AccNo=%s'

    data = (an,)
# Create a cursor object to execute the query
    a = mydb.cursor()

# Executed the query to get customer details
    a.execute(d, data)
    result = a.fetchall()
# Fetched all matching records

    if result:
        # Printed customer details
        for i in result:
            print("The Full Details (Name, AccNo, DOB, Address, PhoneNo, Email, Opening Balance) of Customer with Account Number", an, "is", i)
        main()
    else:
        print("Invalid Input")
        main()

# Function to close an account


def close():
    # Get account number to be closed
    an = input("Enter the Account Number: ")

# SQL queries to delete account from both 'Accounts' and 'Amount' tables
    sql1 = 'DELETE FROM Accounts WHERE AccNo=%s'
    sql2 = 'DELETE FROM Amount WHERE AccNo=%s'
# Tuple containing account number
    data = (an,)
    a = mydb.cursor()

# Executed the queries to delete the account from both tables
    a.execute(sql1, data)
    a.execute(sql2, data)

# Commited the changes to the database
    mydb.commit()

    print("Task Accomplished without Any Error.")
    main()

# Function to display a thank-you message when exiting the program


def tata():
    print()
    print("----------------------------------------------Thanks for trusting ----------------------------------------------------------")
    return

# Main function to display the menu and handle user inputs


def main():

    # Displaying the menu with different options
    print('''
        1. OPENING ACCOUNT
        2. DEPOSIT MONEY
        3. WITHDRAW MONEY
        4. BALANCE ENQUIRY
        5. DISPLAY CUSTOMER DETAILS
        6. CLOSING ACCOUNT
        9. Exit''')
    print()

# Taking user input to select an option
    choice = input("Enter the Number You want to Perform: ")

# Calling corresponding functions based on user input
    if choice == "1":
        OpenAcc()
    elif choice == "2":
        DepositMoney()
    elif choice == "3":
        WithdrawMoney()
    elif choice == "4":
        Balance()
    elif choice == "5":
        CustomerDetails()
    elif choice == "6":
        close()
    elif choice == "9":
        tata()
    else:
        print('Invalid Choice, Sorry!')
        main()


# Password protection: Only allow access if the correct password is entered
x = int(input("Enter the Password\n"))
if x == 123456:
    # Call main() to show the menu if the password is correct
    main()
else:
    print("Please Leave!!")
    # Error message if the password is incorrect

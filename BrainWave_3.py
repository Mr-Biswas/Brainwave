
# Project Title: GUI Based Password Generator
# Import tkinter library to create GUI
from tkinter import *
from tkinter import messagebox
# Import messagebox to show pop-up alerts

# Function to handle the login process


def login():
    username = entry1.get()
    password = entry2.get()

# Get the text entered in the username field
# Get the text entered in the password field

# Checked if both username and password are blank
    if username == " " and password == " ":
        # Showed alert if blank fields are submitted
        messagebox.showinfo("", "Blank Not Allowed")

# Checked if the username and password match the correct credentials
    elif (username == "username" and password == "password"):

        # Show success message if credentials match
        messagebox.showinfo("", "Login Success")

    else:
        # Showed failure message for incorrect credentials
        messagebox.showinfo("", "Incorrect Validation")


# Created the main window for the application
root = Tk()

# Set the window title
# Set the window size (width=500, height=400)
root.title("Password Generator")
root.geometry("500x400")

# Declared global variables for the username and password input fields
global entry1
global entry2

# Created the 'Username' label and set its font, position, and other properties
Label(root, text="Username", font=(
    "Comic Sans MS", 20, "underline")).place(x=20, y=70)

# Created the 'Password' label and set its font, position, and other properties
Label(root, text="Password", font=(
    "Cosmic Sans MS", 20, "underline")).place(x=20, y=120)

# Created an input field (Entry widget) for the username with light green background and sunken border
entry1 = Entry(root, bd=10, width=40, bg="lightgreen", relief='sunken')
entry1.place(x=180, y=70)
# Position the field at x=180, y=70

# Created an input field (Entry widget) for the password with light green background and sunken border
entry2 = Entry(root, bd=10, width=40, bg="lightgreen", relief='sunken')
entry2.place(x=180, y=120)
# Position the field at x=180, y=120

# Created a 'Login' button which calls the login() function when clicked
Button(root, text="Login", command=login, height=3, font=("Times New Roman", 12),
       width=14, bd=6, bg="brown").place(x=150, y=180)

# Started the Tkinter event loop (keeps the window open and listens for user actions)
root.mainloop()

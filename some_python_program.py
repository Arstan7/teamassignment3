# Program description goes here
# Updated on: 11.28.2024
# Updated by: Arstan Domazbekov
#
# Import the tkinter library for creating the GUI
from tkinter import *

# Create the main application window
root = Tk()
root.title("Simple Calculator")  # Set the title of the window to "Simple Calculator"

# Create an input field where users can enter numbers
e = Entry(root, width=35, borderwidth=5)  # Entry widget with width and border specifications
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)  # Position the input field in the grid layout

# Function to handle number button clicks
def button_click(number):
    # Get the current text in the input field
    current = e.get()
    # Clear the input field
    e.delete(0, END)
    # Add the clicked number to the existing text and display it in the input field
    e.insert(0, str(current) + str(number))

# Function to clear the input field
def button_clear():
    e.delete(0, END)  # Remove all text from the input field

# Function to handle operator buttons (+, -, *, /)
def button_operator(operator):
    first_number = e.get()  # Get the current text in the input field
    global f_num  # Declare a global variable to store the first number
    global num_operator  # Declare a global variable to store the operator
    f_num = int(first_number)  # Convert the first number to an integer
    num_operator = operator  # Store the selected operator
    e.delete(0, END)  # Clear the input field to prepare for the second number

# Function to calculate the result when the "=" button is clicked
def button_equal():
    second_number = e.get()  # Get the second number from the input field
    e.delete(0, END)  # Clear the input field
    # Perform the appropriate calculation based on the selected operator
    if num_operator == '+':
        e.insert(0, f_num + int(second_number))  # Addition
    elif num_operator == '-':
        e.insert(0, f_num - int(second_number))  # Subtraction
    elif num_operator == '*':
        e.insert(0, f_num * int(second_number))  # Multiplication
    elif num_operator == '/':
        e.insert(0, f_num / int(second_number))  # Division
    else:
        e.insert(0, "Invalid!!!")  # Handle unexpected operator

# Create number buttons using lambda to pass their respective values to the button_click function
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))

# Create operator buttons
button_add = Button(root, text="+", padx=39, pady=20, command=lambda: button_operator("+"))
button_equal = Button(root, text="=", padx=79, pady=20, command=button_equal)
button_clear = Button(root, text="Clear", padx=79, pady=20, command=button_clear)
button_subtract = Button(root, text="-", padx=40, pady=20, command=lambda: button_operator("-"))
button_multiply = Button(root, text="*", padx=40, pady=20, command=lambda: button_operator("*"))
button_divide = Button(root, text="/", padx=40, pady=20, command=lambda: button_operator("/"))

# Arrange the buttons on the GUI using grid layout
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

# Start the main event loop to display the GUI and handle user interactions
root.mainloop()

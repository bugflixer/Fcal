import os
import math
# Function to clear the screen
def clear_screen():
    os.system('clear')  # For Linux/Unix-based systems

# Function to calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

while True:
    # Clear the screen
    clear_screen()
    
    # Get user input
    num = int(input("\n\033[1;31mEnter a number: \033[36m"))
    
    # Calculate factorial
    result = factorial(num)
    
    # Print result in colorful format
    print("\033[1;31 Factorial of \033[1;36m{}\033[31m is:\033[32m {}".format(num, result))
    
    # Ask the user for the next action
    choice = input("\n\033[1;31m[\033[1;0m+\033[1;31m]\033[1;38m Find another factorial\n\033[1;31m[\033[0m+\033[31m] \033[1;38mExit\n\033[1;32mEnter your choice:\033[1;36m ")
    
    if choice == '2':
        
        print("\n\033[1;35mThanks for using me.....")
        break  # Exit the loop if the user chooses to exit

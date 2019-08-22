# Problem 1:
# Write some Python code that has three variables called greeting, my_name,
# and my_age. Intialize each of the 3 variables with an appropriate value,
# then print out the example below using the 3 variables and
# two different approaches for formatting Strings.
# Using concatenation and the + and 2) Using an f-string. Sample output:
# YOUR_GREETING_VARIABLE YOUR_NAME_VARIABLE!!!
# I hear that you are YOUR_MY_AGE_VARIABLE today!

# greeting = "Hello"
# my_name = "LaVar"
# my_age = "30"

# print(f"{greeting} {my_name} I hear that you are {my_age} today!")

# Problem 2:
# Write some Python code that asks the user for a secret password.
# Create a loop that quits with the user's quit word.
# If the user doesn't enter that word, ask them to guess again.

# userinput = input("Enter the Secret Password")
# secretword = "flash"

# while userinput != "exit":
#     userinput = input("Enter the Secret Password")
#     if userinput != secretword:
#         print("Wrong!")
#     else:
#         print("Correct")

# Problem 3:
# Write some Python code using f-strings that
# prints 0 to 50 three times in a row (vertically).

# number = [0, 50]



# Problem 4:
# Write some Python code that create a random number and stores it in a variable.
# Ask the user to guess the random number.
# Keep letting the user guess until they get it right, then quit.
import random

guesser = 1
randomnumber = random.randint[1, 10]
userinput = input("Guess the number 1-10")
while userinput != randomnumber:
    userinput = int(input("Enter your guess"))
if guesser != randomnumber:
    print("Wrong!")
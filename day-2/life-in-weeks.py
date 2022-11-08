# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

# Example Input
# 56

# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.


age = input("What is your current age? ")

#Write your code below this line 👇
remaining_age = 90 - int(age)

days_left = 365*remaining_age
weeks_left = 52*remaining_age
months_left = 12*remaining_age

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")

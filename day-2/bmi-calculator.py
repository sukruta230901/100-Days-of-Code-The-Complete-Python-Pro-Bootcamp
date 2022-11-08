# PEMDASLR (PARENTHESES, EXPONENTS, MULTIPLICATION, DIVISION, ADDITION, SUBTRACTION, LEFT -> RIGHT) priority level: (), **, * /, + -

# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# Example Input
# weight = 80
# height = 1.75

# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Write your code below this line
bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

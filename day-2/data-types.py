# Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
# Example Input
# 39

# Example Output
# 3 + 9 = 12
# 12

two_digit_number = input("Type a two digit number: ")

#Write your code below this line 👇
num1 = two_digit_number[0]
num2 = two_digit_number[1]
add = int(num1) + int(num2)
print(add)

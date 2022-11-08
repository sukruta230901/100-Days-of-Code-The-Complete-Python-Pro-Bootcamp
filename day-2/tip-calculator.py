# https://replit.com/@SukrutaPardeshi/tip-calculator-start?v=1

#If the bill was $150.00, split between 5 people, with 12% tip. 

#For example the total bill was &150.00 and the bill is to split between 5 peoples then, each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. 

#Write your code below this line 👇
total_bill = input("What was the total bill? $")
tip_given = input ("What percentage tip would you like to give? 10, 12, or 15? ")
people_to_split = input("How many people to split the bill? ")

people_to_split_int = int(people_to_split)
percentage_tip = int(tip_given)/100
each_person_tip = 1 + float(percentage_tip)
total_bill_float = float(total_bill)
each_person_bill = (total_bill_float / people_to_split_int) * each_person_tip

#Formatting the result to 2 decimal places
each_person_bill_to_pay = "{:.2f}".format(each_person_bill)

#printing the result
print(f"Each person should pay: ${each_person_bill_to_pay}")

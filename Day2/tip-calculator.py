print("Welcome To The Tip Calculator!!")
bill = float(input("What was the total bill? $"))
tipPercentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))


tipAmount = (bill + (bill * float(tipPercentage/100)))/people;

print(f"Each person should pay ${round(tipAmount, 2)}")
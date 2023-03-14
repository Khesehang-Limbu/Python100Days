print("Welcome to Python pizza deleveris!")
size = input("What size pizza do you want? L, M, S ? ")
add_peperroni = input("Do you want to add peperroni? Y or N? ")
extra_cheese = input("Do you want to add extra cheese? Y or N? ")

small = 15
medium = 20
large = 25
bill = 0


if (size == "L" or size == "l"):
    if (add_peperroni == "Y" or add_peperroni == "y" ):
        large+=3
    if (extra_cheese == "Y" or extra_cheese == "y"):
        large = large + 1
    print(f"Your total bill is ${large}")
elif (size == "M" or size == "m"):
    if (add_peperroni == "Y" or add_peperroni == "y" ):
        medium+=3
    if (extra_cheese == "Y" or extra_cheese == "y"):
        medium+=1
    print(f"Your total bill is ${medium}")
else:
    if (add_peperroni == "Y" or add_peperroni == "y" ):
        small+=3
    if (extra_cheese == "Y" or extra_cheese == "y"):
        small+=1
    print(f"Your total bill is ${small}")
    

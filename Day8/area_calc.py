from math import ceil

def cans_calulator(height, width, coverage):
    return ceil((height*width)/coverage)


height = float(input("Enter height in meters(m) : "))
width = float(input("Enter width in meters(m) : "))
coverage = 5

print(f"YOu'll require {cans_calulator(height=height, width=width, coverage=coverage)} cans of paint")
heights = input("Enter the list of heights in cm, separated by space : ").split();

sum = 0
count = 0
for height in heights:
    sum += int(height)
    count+=1
    
print(f"The average height is {round(sum/count)} cm")    
values = input("Enter the values, each separated by a space : ").split()

max = int(values[0])

for i in range(0, len(values)):
    if (max < int(values[i])):
        max = int(values[i])

print(f"The maximum value is {max}")
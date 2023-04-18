import pandas

# file1 = pandas.read_csv("file1.txt")
# file2 = pandas.read_csv("file2.txt")

with open("file1.txt") as file1:
    num1 = file1.readlines()
    num1_list = [int(num.strip()) for num in num1]

with open("file2.txt") as file2:
    num2 = file2.readlines()
    num2_list = [int(num.strip()) for num in num2]

intersection_list = [num for num in num2_list if (num in num1_list)]
print(intersection_list)





































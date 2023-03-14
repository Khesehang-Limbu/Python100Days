import random

row1 = ["☐", "☐", "☐"]
row2 = ["☐", "☐", "☐"]
row3 = ["☐", "☐", "☐"]
rows = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}\n")

position = input("Enter the location where you want to place the treasure (column then row): ")

#11
row = int(position[0])+1
col = int(position[1])+1
rows[row-2][col-2] = "X";

print(f"{row1}\n{row2}\n{row3}\n")
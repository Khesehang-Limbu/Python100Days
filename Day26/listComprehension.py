# using list compreshension, we can shorten the code required for creating a new list from the previous list
# Besides lists, we can also use this python specific feature for other sequential structures like string
# Python sequences are strings, tuple, list, range

# Without using list comprehension
numbers = [1, 2, 3]
new_list = []

for n in numbers:
    new_list.append(n+1)

print(new_list)

# Using List Comprehension, it is as easy as:
# The syntax is like, new_list_name = [new_item for item in list]
new_numbers = [n+2 for n in numbers]

print(new_numbers)

name = "khesehang"

letters_list = [letter for letter in name]
print(letters_list)

doubled_numbers = [2*n for n in range(1, 5)]
print(doubled_numbers)

names = ["Khesehang", "Amar", "Karuna", "Namrata"]

short_names = [name for name in names if (len(name) <= 6)]
print(short_names)

uppercase_names = [name.upper() for name in names if len(name) >= 6]
print(uppercase_names)
def title_format(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    return f_name + " " + l_name
f_name = input("Enter first name : ")
l_name = input("Enter last name : ")

print(title_format(f_name, l_name))
############DEBUGGING#####################
# def my_function():
#     for i in range(1, 20+1): #Since the upper bound of the range function is omitted, the condition is never true for i == 20; so, it should be 1 above the initial upper bound
#         if i == 20: 
#             print("You got it!")
            
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)#initially (1, 6)
# # if dice_num == 6: The bug index out of range only occurs when the random integer value is 6. Since the index of a list data structrue begins from 0, to represent 6 numbers we should have the upper bound equal to 5 i.e. (0, 5)
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth? "))
# if year >= 1980 and year <= 1994:#The problem here is that the condition, year == 1980 and 1994 are never checked, hence the behavior isn't there for those corresponding values, to fix it we need to put an equal to sign in front of the numbers
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = int(input("How old are you?"))#Here, we didn't type cast the oputput of input() function, which is String to a integer.
# if age > 18:
#     print(f"You can drive at age {age}.")#Here the indententation wasn't there and the print statement needs to be a f string to output the desired result

# #Print is Your Friend
# pages = 0
# word_per_page = 0

# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))#Here, instead of an equals to operator, there was a relational operator, hence  the error


# total_words = pages * word_per_page
# print(total_words)

# #Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)#Here the append method was outside the loop, hence only the last list item got multiplied by 2 and appended to the list
#   print(b_list)

# mutate([1,2,3,5,8,13])
import random

people = input("Enter the names of the people, each separated by a comma (,) : ")
people = people.split(",");

randomIndex = random.randint(0, len(people)-1)
print(len(people)-1)
print(f"{people[randomIndex]} will pay the bill")
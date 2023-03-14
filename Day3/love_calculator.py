print("Welcome to Love Calculator!!")
name1 = input("Enter your name : ").lower()
name2 = input("Enter your partner's name : ").lower()

name = name1 + name2

T = name.count("t")
R = name.count("r")
U = name.count("u")
E = name.count("e")

L = name.count("l")
O = name.count("o")
V = name.count("v")
E = name.count("e")

score = str(T+R+U+E) + str(L+O+V+E)
score = int(score)

if (score < 10 or score > 90):
    print(f"Your score is {score}, you go together like coke and mentos")
elif (score >= 40 and score <= 50 ):
    print(f"Your score is {score}, you are alright together")
else:
    print(f"Your score is {score}")
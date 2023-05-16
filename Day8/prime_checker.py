number = int(input("Enter the number to check : "))

def prime_checker(num): #1
    isPrime = True
    for i in range(2, num):
        if (num%i == 0):
            isPrime = False
            return isPrime
    return isPrime

if prime_checker(number):
    print("Prime Number")
else:
    print("Not a prime number") 
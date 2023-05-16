def add(*args):
    # Alternatively
    # sum = 0
    # for num in args:
    #     sum+=num

    # We can use the sum function because the *args is a tuple (1,2) It is the way of defining the unlimited positional arguments
    print(args[1])
    return sum(args)


total = add(1, 2, 3, 4, 5, 6, 7)
print(total)

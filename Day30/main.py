# dict = {"key" : 1}
# try:
#     file = open("./data.txt")
#     file.read()
#     dict["key"]
# except FileNotFoundError:
#     file = open("./data.txt", mode= "a")
#     file.write("My Name is Khesehang")
# except KeyError as error_message:
#     print(f"The {error_message} is not found")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()

weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

if height > 3:
    raise ValueError("Humans cannot have such unimaginable height"
                     )
bmi = weight/ height ** 2

print(bmi)
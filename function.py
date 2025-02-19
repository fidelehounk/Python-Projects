def hello():
    print("Hello World") 
    return 42

def hola():
    print("Hola")
    return 13

choice = int(input ("Please choose 1 or 2: "))

if choice == 1:
    greeting = hello
    greeting = hello
else:
    greeting = hola

magic_number = greeting()
print(magic_number)
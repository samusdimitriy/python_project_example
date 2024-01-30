age = input("How old are you? ")
try:
    age = int(age)
    if age >= 18:
        print("You are an adult")
    else:
        print("You are not an adult")
except ValueError:
    print(f"{age} is not a number")
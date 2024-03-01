message = "Hello Mr. "

def greet(name):
    global message
    message = "Hi Mr. "
    print(message + name)

def greet1(name):
    random_variable = 14
    print(message + name)


greet1("Smith")

greet("John")
print(locals())



def is_check_name(fullname, first_name):
    return fullname.lower().startswith(first_name.lower())

fullname = "John Doe"
first_name = "John"

print(is_check_name(fullname, first_name))
username = input("Enter your user name please: ")
password = input("Enter your user password please: ")

if "admin" in username:
    if password == "qwerty":
        print(f"Login successful! Welcome {username}")
    elif password == "12345":
        print("Week password")
    else:
        print("incorrect password")
elif "guest" in username:
    if password == "guest123":
        print(f"Login successful! Welcome {username}")
    else:
        print("incorrect password")
else: 
    print("only guests or admins allowed")

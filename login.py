try:
    username=input("Enter username:")
    password=input("Enter password:")
    if username=="harini" and password=="456":
        print("LOGIN SUCCESSFULL")
    elif username==" " or password==" ":
        raise ValueError("Empty input not allowed")
    else:
        print("Invalid credentials")
except ValueError as e:
    print("Error:",e)
finally:
    print("completed execution")


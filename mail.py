try:
    email=input("Enter your email:")
    if "@" not in email or "." not in email:
        raise Exception("Invalid email format")
    print("Valid email")
except Exception as e:
    print("Error:",e)
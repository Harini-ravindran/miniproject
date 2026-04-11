try:
    correctpin=987654;
    attempts=3
    while attempts>0:
        pin=int(input("Enter your pin:"))
        if pin==correctpin:
            print("Access granted")
            break
        else:
            attempts-=1
            print("wrong pin,Attempts left:",attempts)
    if attempts==0:
        print("Card bloacked sorry :)")
except ValueError:
    print("Invalid PIN format")
except Exception as e:
    print("Error:",e)

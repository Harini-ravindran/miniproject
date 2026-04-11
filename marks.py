try:
    mark=int(input("Enter mark:"))
    if mark < 0 or mark > 100:
        raise Exception("Invalid mark range:")
    if mark>=90:
        print("Grade:A")
    elif mark>=75:
        print("Grade:B")
    elif mark>=50:
        print("Grade:C")
    else:
        print("FAIL")
except ValueError:
    print("Invalid syntax")


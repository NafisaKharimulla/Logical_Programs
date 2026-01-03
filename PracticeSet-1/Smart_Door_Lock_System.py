pin=1234
attempt1=int(input("Enter the pin"))
if attempt1==pin:
    print("Access Granted")
else:
    attempt2=int(input("ENter again"))
    if attempt2==pin:
        print("Access granted");
    else:
        attempt3=int(input("Enter pin"))
        if attempt3==pin:
            print("Access Granted")
        else:
            print("Locked")
            

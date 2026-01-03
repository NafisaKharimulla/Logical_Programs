distance=int(input("Enter distance in kilometers"))
age=int(input("How old are you"))
fare=distance*2
if(age>50):
    fare=fare-0.3*fare
elif age<12:
    fare=fare-0.5*fare
else:
    fare
print(int(fare))



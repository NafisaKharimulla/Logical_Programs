T = int(input())
t = T % 90
if t == 0:
    t = 90

if 1 <= t <= 30:
    print("RED")
elif 31 <= t <= 45:
    print("YELLOW")
else:
    print("GREEN")


''' Pattern Starts for every 
90 sec so insted of checking for every 500 or 1000 
we just divide time by 90
'''
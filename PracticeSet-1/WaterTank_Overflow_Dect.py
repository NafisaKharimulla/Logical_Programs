N = int(input("Enter number of minutes: "))
water_list = list(map(int, input("Enter inflow values: ").split()))

tank_capacity = 1000
current_water = 0

for minute in range(N):
    current_water = current_water + water_list[minute]

    if current_water > tank_capacity:
        print(minute + 1)
        break

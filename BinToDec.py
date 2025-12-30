binary = input().strip()
decimal = 0
for digit in binary:
    decimal = decimal * 2 + int(digit)

print(decimal)


'''
Logic:
Start with decimal = 0

For each binary digit, multiply decimal by 2 → shift left by 1 bit

Add the current digit (0 or 1)
'''
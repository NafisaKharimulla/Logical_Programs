balance = int(input().strip())
n = int(input().strip())

for _ in range(n):
    amount = int(input().strip())

    if amount % 100 == 0 and amount <= balance:
        balance -= amount
        print("SUCCESS")
    else:
        print("FAILED")

print(balance)

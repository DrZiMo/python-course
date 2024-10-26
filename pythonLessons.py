wallet = 25
socks = 0

for price in range(10):
    if wallet >= price:
        wallet = wallet - price
        socks = socks + 1
    else:
        break

print("I have", wallet, "dollars")
print("and", socks, "socks")

time = 3

for n in range(3):
    if n < time:
        print(n)
    elif n == time:
        print("go")

number = 27
steps = 0

for i in range(200):
    if number == 1:
        break
    elif number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    steps = steps + 1

if number == 1:
    print("it took", steps, "steps")
else:
    print("number didn't reach 1 yet")

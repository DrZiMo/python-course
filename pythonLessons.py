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
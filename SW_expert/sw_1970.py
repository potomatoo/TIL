flag = True
for a in range(1000,10000):
    for b in range(1000,10000):
        if a**2 + b == 97540808 and b **2 +a == 29516500:
            flag = False
            break
    if flag == False:
        break

print(a)
print(b)
N = int(input())
spot = list(map(int, input().split()))
B, C = map(int, input().split())
people = N
for i in range(len(spot)):
    if spot[i] - B <= 0:
        spot[i] = 0
        continue
    spot[i] = spot[i] - B

for i in range(len(spot)):
    if spot[i] % C:
        people += (spot[i] // C) + 1
    else:
        people += (spot[i] // C)
print(people)
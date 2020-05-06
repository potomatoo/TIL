from _collections import deque

one = deque()
two = deque()
three = deque()
four = deque()

for i in range(4):
    tire = input()
    for j in range(8):
        if i == 0:
            one.append(tire[j])
        if i == 1:
            two.append(tire[j])
        if i == 2:
            three.append(tire[j])
        if i == 3:
            four.append(tire[j])

factory = deque()
factory.append(one)
factory.append(two)
factory.append(three)
factory.append(four)

K = int(input())

for _ in range(K):
    n, where = map(int,input().split())

    # 2, 6이 맞닿는 부분
    rope = [one[2], two[6], two[2], three[6], three[2], four[6]]

    factory[n-1].rotate(where)
    if n == 1:
        if rope[0] != rope[1]:
            factory[1].rotate(-where)
            if rope[2] != rope[3]:
                factory[2].rotate(where)
                if rope[4] != rope[5]:
                    factory[3].rotate(-where)

    if n == 2:
        if rope[2] != rope[3]:
            factory[2].rotate(-where)
            if rope[4] != rope[5]:
                factory[3].rotate(where)
        if rope[0] != rope[1]:
            factory[0].rotate(-where)

    if n == 3:
        if rope[2] != rope[3]:
            factory[1].rotate(-where)
            if rope[0] != rope[1]:
                factory[0].rotate(where)
        if rope[4] != rope[5]:
            factory[3].rotate(-where)

    if n == 4:
        if rope[4] != rope[5]:
            factory[2].rotate(-where)
            if rope[2] != rope[3]:
                factory[1].rotate(where)
                if rope[0] != rope[1]:
                    factory[0].rotate(-where)

ans = 0

if factory[0][0] == '1':
    ans += 1
if factory[1][0] == '1':
    ans += 2
if factory[2][0] == '1':
    ans += 4
if factory[3][0] == '1':
    ans += 8
print(ans)





def permutation(arr):
    result = [arr[:]]
    c = [0] * len(arr)
    i = 0
    while i < len(arr):
        if c[i] < i:
            if i % 2 == 0:
                arr[0], arr[i] = arr[i], arr[0]
            else:
                arr[c[i]], arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            c[i] += 1
            i = 0
        else:
            c[i] = 0
            i += 1
    return result

def multi_zero(ls):
    result = []
    for y in range(len(ls)):
        cal = ls[y][0]
        for x in range(1, len(ls[y])):
            if multi <= x < multi + div and cal < 0:
                cal = -((-cal) // ls[y][x])
            elif multi <= x < multi + div and cal >= 0:
                cal = cal // ls[y][x]
            elif multi + div <= x < multi + div + plus:
                cal += ls[y][x]
            elif multi + div + plus <= x < multi + div + plus + minus:
                cal -= ls[y][x]
        result.append(cal)
    return result

def not_multi_zero(ls):
    result = []
    for y in range(len(ls)):
        cal = ls[y][0]
        for x in range(1, len(ls[y])):
            if x < multi:
                cal *= ls[y][x]
            elif multi <= x < multi + div and cal < 0:
                cal = -((-cal) // ls[y][x])
            elif multi <= x < multi + div and cal >= 0:
                cal = cal // ls[y][x]
            elif multi + div <= x < multi + div + plus:
                cal += ls[y][x]
            elif multi + div + plus <= x < multi + div + plus + minus:
                cal -= ls[y][x]
        result.append(cal)
    return result

N = int(input())
num = list(map(int,input().split()))
plus, minus, multi, div = map(int,input().split())
ls = permutation(num)
print(ls)
if multi:
    result = not_multi_zero(ls)
    print(max(result))
    print(min(result))
else:
    result = multi_zero(ls)
    print(max(result))
    print(min(result))

print(1//2+3+4-5*6)
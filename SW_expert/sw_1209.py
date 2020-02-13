import sys
sys.stdin = open('./input/input_1209.txt', 'r')

def my_max(ls):
    mmax = ls[0]
    for i in range(len(ls)):
        if ls[i] > mmax:
            mmax = ls[i]
    return mmax

for tc in range(10):
    n = int(input())
    arr = []
    for i in range(100):
        numbers = list(map(int, input().split()))
        arr.append(numbers)

    colum = []
    row = []
    degak1 = 0
    degak2 = 0

    for y in range(len(arr)):
        sero = 0
        garo = 0
        for x in range(len(arr[y])):
            if x == y:
                degak1 += arr[x][y]
            sero += arr[x][y]
            garo += arr[y][x]
        colum.append(sero)
        row.append(garo)

    for y in range(len(arr)):
        for x in range(99,-1,-1):
            if y + x == 100:
                degak2 += arr[y][x]
                break
    result = my_max([my_max(colum), my_max(row), degak1, degak2])
    print('#{} {}'.format(tc+1, result))




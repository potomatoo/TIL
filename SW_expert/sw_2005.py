TC = int(input())
for tc in range(TC):
    n = int(input())
    print('#%s' % (tc + 1))
    pascal = []
    for i in range(1, n + 1):
        result = []
        for j in range(i):
            result.append(1)
        pascal.append(result)

    for i in range(len(pascal)):
        for j in range(1, len(pascal[i]) - 1):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    for i in range(len(pascal)):
        for j in range(len(pascal[i])):
            print(pascal[i][j], end=' ')
        print()
TC = int(input())
a = 1
for tc in range(TC):
    N = int(input())
    ls = input().split()
    ls = list(map(int, ls))
    ls.sort()
    half = int(len(ls)/2)
    ls1 = ls[:half]
    ls2 = ls[half:len(ls)]
    ls2.sort(reverse=True)
    print('#%d' % a, end = ' ')
    for i in range(5):
        print(ls2[i], ls1[i], end = ' ')
    a += 1
    print()
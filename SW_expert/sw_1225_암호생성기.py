import sys
sys.stdin = open('./input/input_1225.txt','r')

for tc in range(10):
    N = int(input())
    nums = list(map(int,input().split()))
    i = 1
    while True:
        if nums[-1] == 0 or nums[-1] < 0:
            nums[-1] = 0
            break
        if i == 6:
            i = 1
        v = nums.pop(0)
        nums.append(v - i)
        i += 1
    print('#%d'%(tc+1), end= ' ')
    print(*nums)
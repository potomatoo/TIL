import sys
sys.stdin = open('./input/input_6485.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    C = [0] * 5001
    for _ in range(N):
        A, B = map(int,input().split())
        for i in range(A,B+1):
            C[i] += 1
    P = int(input())
    print('#%d'%(tc+1), end= ' ')
    for i in range(P):
        k = int(input())
        if i == P-1:
            print(C[k])
        else:
            print(C[k], end = ' ')
import sys
sys.stdin = open('./input/input_1959.txt', 'r')

TC = int(input())
for tc in range(TC):
    a, b = map(int, input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if b > a:
        A, B = B, A
    result = []
    for j in range(len(A)-len(B)+1):
        multi1 = 0
        for i in range(len(B)):
            multi2 = A[i+j] * B[i]
            multi1 += multi2
        result.append(multi1)
    print('#{} {}'.format(tc+1, max(result)))
def Hanoi(A, B, C, N):
    if N == 1:
        print(A,C)
        return
    Hanoi(A, C, B, N-1)
    Hanoi(A, B, C, 1)
    Hanoi(B, A, C, N-1)


N = int(input())
print(2**N-1)
Hanoi('1','2','3',N)



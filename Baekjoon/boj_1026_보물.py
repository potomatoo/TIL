N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
answer = 0
while N:
    answer += (max(B) * min(A))
    B.pop(B.index(max(B)))
    A.pop(A.index(min(A)))
    N -= 1
print(answer)






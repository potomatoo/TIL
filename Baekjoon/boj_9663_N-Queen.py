def nqueen(r):
    global answer
    if r == N:
        answer += 1
        return
    for c in range(N):
        if not col[c] and not dia_1[r+c] and not dia_2[N-1-(r-c)]:
            col[c] = 1
            dia_1[r+c] = 1
            dia_2[N-1-(r-c)] = 1
            nqueen(r+1)
            col[c] = 0
            dia_1[r + c] = 0
            dia_2[N - 1 - (r - c)] = 0

N = int(input())
col = [0] * N
dia_1 = [0] * ((2*N)-1)
dia_2 = [0] * ((2*N)-1)
answer = 0
nqueen(0)
print(answer)
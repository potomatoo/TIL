import sys
sys.stdin = open('./input/input_4012.txt','r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    f_map = []
    for _ in range(N):
        line = list(map(int,input().split()))
        f_map.append(line)

    c = [x for x in range(0,N)]
    n = len(c)
    c_ls = []
    for i in range(1 << n):
        line = []
        for j in range(n):
            tf = i & (1 << j)
            if tf:
                line.append(c[j])
        if len(line) == N//2:
            c_ls.append(line)

    for food1 in c_ls:
        for food2 in c_ls:
            if sorted(food1+food2) != c:
                continue
            for i in food1:
                for j in food1:
                    if i == j:
                        continue
                    else:
                        f_map[i][j]
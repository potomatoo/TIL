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

    diff = []
    for i in range(len(c_ls)//2):
        food1 = c_ls[i]
        food2 = c_ls[-(i+1)]
        a_taste = 0
        b_taste = 0
        for y1 in food1:
            for x1 in food1:
                if y1 != x1:
                    a_taste += f_map[y1][x1]
        for y2 in food2:
            for x2 in food2:
                if y2 != x2:
                    b_taste += f_map[y2][x2]

        diff.append(abs(a_taste - b_taste))
    print('#{} {}'.format(tc+1,min(diff)))

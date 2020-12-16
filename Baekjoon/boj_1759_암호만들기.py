def password(k):
    if k == L:
        mo_cnt = 0
        za_cnt = 0
        for i in range(len(order)):
            if order[i] in moem:
                mo_cnt += 1
            else:
                za_cnt += 1
        if za_cnt > 1 and mo_cnt > 0:
            for i in range(len(order)):
                if i == len(order) - 1:
                    print(order[i])
                else:
                    print(order[i],end='')
    else:
        for i in range(C):
            if visit[i] == 1:
                continue
            if len(order) > 0:
                if order[-1] > alpa[i]:
                    continue
            visit[i] = 1
            order.append(alpa[i])
            password(k+1)
            visit[i] = 0
            order.pop()


L, C = map(int,input().split())
alpa = input().split()
alpa.sort()
order = []
moem = ['a','e','i','o','u']
visit = [0] * C
password(0)

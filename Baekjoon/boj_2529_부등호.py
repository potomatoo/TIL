def permutiation(k,num):
    global flag
    if flag == True:
        if k == m:
            if cal[m-2] == '<':
                if order[-2] < order[-1]:
                    for i in range(len(order)):
                        print(order[i],end='')
                    flag = False

            if cal[m-2] == '>':
                if order[-2] > order[-1]:
                    for i in range(len(order)):
                        print(order[i], end='')
                    flag = False

        else:
            for i in range(len(num)):
                if visit[i] == 1:
                    continue
                if len(order) > 1:
                    if cal[k - 1] == '<':
                        if order[k - 3] > order[k - 2]:
                            continue
                    if cal[k - 1] == '>':
                        if order[k - 3] < order[k - 2]:
                            continue
                order.append(num[i])
                visit[i] = 1
                permutiation(k+1,num)
                visit[i] = 0
                order.pop()

N = int(input())
cal = input().split()
flag = True
m = N+1
order = []
num = [9,8,7,6,5,4,3,2,1,0]
num2 = [0,1,2,3,4,5,6,7,8,9]
visit = [0] * len(num)
permutiation(0,num)
flag = True
print()
permutiation(0,num2)


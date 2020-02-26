def permutiation(k,num):
    global flag
    if flag == True:
        if k == m:
            for i in range(len(order)):
                print(order[i],end='')
                flag = False
        else:
            for i in range(len(num)):
                if visit[i] == 1:
                    continue
                if len(order) > 0:
                    if cal[len(order)-1] == '<' and order[-1] > num[i]:
                        continue
                    if cal[len(order)-1] == '>' and order[-1] < num[i]:
                        continue
                order.append(num[i])
                visit[i] = 1
                permutiation(k+1,num)
                visit[i] = 0
                order.pop()

N = int(input())
cal = input().split()
m = N+1
order = []
flag = True
num = [9,8,7,6,5,4,3,2,1,0]
visit = [0] * len(num)
permutiation(0,num)
num2 =[0,1,2,3,4,5,6,7,8,9]
visit2 = [0] * len(num2)
flag = True
print()
permutiation(0,num2)


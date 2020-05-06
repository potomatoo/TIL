def find_seven(k):
    global flag
    if flag:
        if k == 7:
            if sum(order) == 100:
                order.sort()
                for i in range(len(order)):
                    print(order[i])
                flag = False
        else:
            for i in range(9):
                if visit[i] == 1:
                    continue
                visit[i] = 1
                order.append(people[i])
                find_seven(k+1)
                visit[i] = 0
                order.pop()
people = []
for _ in range(9):
    people.append(int(input()))
order = []
visit = [0] * 9
flag = True
find_seven(0)


TC = int(input())
for tc in range(TC):
    n = int(input())
    num_ls = list(map(int,input().split()))
    result = []
    for i in range(len(num_ls)-1):
        for j in range(i+1, len(num_ls)):
            if i == j:
                continue
            result.append(num_ls[i]*num_ls[j])

    result = list(map(str,result))
    danjo = []
    for i in range(len(result)):
        if len(result[i]) == 1:
            continue
        sum = 0
        for j in range(len(result[i])-1):
            if int(result[i][j]) > int(result[i][j+1]):
                sum += 1
        if sum == 0:
            danjo.append(int(result[i]))

    if len(danjo) == 0:
        print('#{} {}'.format(tc+1, -1))
    else:
        print('#{} {}'.format(tc+1,max(danjo)))

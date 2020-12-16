import sys
sys.stdin = open('./input/input_5215.txt','r')

def subset(data):
    n = len(data)
    result = []
    for i in range(1 << n):
        one = []
        for j in range(n):
            tf = i & (1 << j)
            if tf:
                one.append(data[j])
        result.append(one)
    return result

TC = int(input())
for tc in range(TC):
    N, limit = map(int,input().split())
    data = []
    for _ in range(N):
        data.append(list(map(int,input().split())))
    score, cal = [], []
    for i in range(len(data)):
        score.append(data[i][0])
        cal.append(data[i][1])
    s = subset(score)
    c = subset(cal)
    max_cal = []
    max_n = []
    for i in range(len(c)):
        if sum(c[i]) <= limit:
            max_cal.append(c[i])
            max_n.append(s[i])
    nn = sum(max_n[1])
    for i in range(len(max_n)):
        if nn < sum(max_n[i]):
            nn = sum(max_n[i])
    print('#{} {}'.format(tc+1, nn))


import sys
sys.stdin = open('./input/input_1221.txt','r')

TC = int(input())
solars = [('ZRO',0), ('ONE',1), ('TWO',2), ('THR',3),('FOR',4), ('FIV', 5),
         ('SIX', 6), ('SVN', 7), ('EGT', 8), ('NIN', 9)]
for tc in range(TC):
    cnt = [0] * 10
    n, c = map(str,input().split())
    c = int(c)
    data = list(map(str, input().split()))
    for solar, i in solars:
        for k in range(len(data)):
            if data[k] == solar:
                cnt[i] += 1
    result = ''
    for solar, i in solars:
        result += (solar+' ')*cnt[i]

    print(n)
    print(result[:-1])




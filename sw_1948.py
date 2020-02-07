import sys
sys.stdin = open('input_1948.txt','r')
import datetime
TC = int(input())
for tc in range(TC):
    day = list(map(int, input().split()))
    first = day[:2]
    second = day[2:]

    result = datetime.datetime(2020,second[0],second[1]) - datetime.datetime(2020,first[0],first[1])
    print('#{} {}'.format(tc+1, int(str(result)[:3])+1))

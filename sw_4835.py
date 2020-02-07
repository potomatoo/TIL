import sys
sys.stdin = open('input_4835.txt','r')

TC = int(input())
for tc in range(TC):
    number, j = map(int,input().split())
    numbers = list(map(int,input().split()))
    result = []
    for i in range(number-(j-1)):
        sum_number = 0
        for k in range(i,i+j):
            sum_number += numbers[k]
        result.append(sum_number)

    print('#{} {}'.format(tc+1, max(result)-min(result)))


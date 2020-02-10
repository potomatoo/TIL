import sys
sys.stdin = open('input_3376.txt', 'r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    result = [1,1,1]
    j = 1
    for i in range(N-3):
        result.append(result[i] + result[j])
        j += 1
    print('#{} {}'.format(tc+1,result[-1]))


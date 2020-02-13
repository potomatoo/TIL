import sys
sys.stdin = open('./input/input_금속막대.txt', 'r')

TC = int(input())
for tc in range(TC):
    n = int(input())
    numbers = list(map(int,input().split()))
    nasa = [[numbers[i], numbers[i+1]] for i in range(0, len(numbers)-1, 2)]
    front = [numbers[i] for i in range(0,len(numbers),2)]
    back =  [numbers[i] for i in range(1,len(numbers),2)]
    for i in range(len(nasa)):
        if nasa[i][0] not in back:
            nasa[0], nasa[i] = nasa[i], nasa[0]

    for i in range(len(nasa)):
        for j in range(i+1,len(nasa)):
            if nasa[i][1] == nasa[j][0]:
                nasa[i+1], nasa[j] = nasa[j], nasa[i+1]
                break
    print('#{}'.format(tc+1), end=' ')
    for i in range(len(nasa)):
        for j in range(len(nasa[i])):
            print('{}'.format(nasa[i][j]), end=' ')
    print()

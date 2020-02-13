import sys
sys.stdin = open('./input/input_1206.txt','r')

for tc in range(10):
    TC = int(input())
    building = list(map(int,input().split()))
    result = 0
    for i in range(2, len(building)-2):
        if building[i] > building[i+1] and building[i] > building[i+2]\
                and building[i] > building[i-1] and building[i] > building[i-2]:
            result += building[i] - max(building[i-2], building[i-1], building[i+1], building[i+2])
    print('#{} {}'.format(tc+1, result))




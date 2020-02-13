import sys
sys.stdin = open('./input/input_4831.txt','r')

TC = int(input())
for tc in range(TC):
    K, N, M = map(int,input().split())
    charge = list(map(int,input().split()))
    result = 0
    cnt = 0
    flag = 1
    for i in range(len(charge)):
        print(result)
        if result + K > N:
            break
        result += K
        if result in charge:
            cnt += 1
        else:
            for j in range(len(charge)):
                if charge[j] - K > charge[j - 1]:
                    cnt = 0
                    flag = 0
                    break
                if j == len(charge)-3 and charge[j] < result:
                    result = charge[-1]
                    cnt += 1
                    break
                if charge[j] > result:
                    result = charge[j-1]
                    cnt += 1
                    break
            if flag == 0:
                break

    print('#{} {}'.format(tc+1, cnt))









import sys
sys.stdin = open('./input/input_5203.txt', 'r')

TC = int(input())

for tc in range(TC):
    flag2 = True
    flag = True
    card = list(map(int,input().split()))
    one = [[] for _ in range(11)]
    two = [[] for _ in range(11)]
    for i in range(len(card)):
        if i == 0:
            one[card[i]].append(card[i])
        elif i == 1:
            two[card[i]].append(card[i])
        elif not i % 2:
            one[card[i]].append(card[i])
        elif i % 2:
            two[card[i]].append(card[i])

        for j in range(8):
            if len(one[j]) > 0 and len(one[j+1]) and len(one[j+2]):
                print(f'#{tc+1} {1}')
                flag = False
                flag2 = False

                break
            if len(two[j]) > 0 and len(two[j+1]) and len(two[j+2]):
                print(f'#{tc+1} {2}')
                flag = False
                flag2 = False

                break

        if not flag2:
            break

        if not flag:
            for k in range(11):
                if len(one[k]) >= 3:
                    print(f'#{tc+1} {1}')
                    flag2 = False
                    break
                if len(two[k]) >= 3:
                    print(f'#{tc+1} {2}')
                    flag2 = False
                    break
            if not flag2:
                break

    if flag == False:
        print(f'#{tc+1} {0}')



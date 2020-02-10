import sys
sys.stdin = open('./input/input_4047.txt', 'r')

TC = int(input())

for tc in range(TC):
    c = input()
    cards = []
    SDHC = [13, 13, 13, 13]
    flag = True
    for i in range(0,len(c),3):
        cards.append(c[i:i+3])

    for i in range(len(cards)-1):
        for j in range(i+1,len(cards)):
            if cards[i] == cards[j]:
                print('#{} {}'.format(tc+1, 'ERROR'))
                flag = False
                break
    if flag == False:
        continue
    shape_cnt = [0,0,0,0]
    for card in cards:
        if card[0] == 'S':
            shape_cnt[0] += 1
        if card[0] == 'D':
            shape_cnt[1] += 1
        if card[0] == 'H':
            shape_cnt[2] += 1
        if card[0] == 'C':
            shape_cnt[3] += 1
    print('#%d'%(tc+1), end=' ')
    for i in range(len(SDHC)):
        if i == len(SDHC) -1:
            print(SDHC[i] - shape_cnt[i])
        else:
            print(SDHC[i] - shape_cnt[i], end=' ')
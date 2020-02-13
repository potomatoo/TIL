import sys
sys.stdin = open('./input/input_4834.txt','r')

TC = int(input())
for tc in range(TC):
    n = int(input())
    card = input()
    check = list(set(card))
    cnt = 0
    max_num = 0
    for c in check:
        if card.count(c) > cnt:
            cnt = card.count(c)
            max_num = int(c)
        elif card.count(c) == cnt:
            if max_num < int(c):
                max_num = int(c)
    print(card, check)
    print('#{} {} {}'.format(tc+1, max_num, cnt))


import sys
sys.stdin = open('./input/input_4865.txt','r')

TC = int(input())
for tc in range(TC):
    words = []
    w_dic = {}

    for _ in range(2):
        words.append(input())

    for w1 in words[0]:
        for w2 in words[1]:
            w_dic[w1] = words[1].count(w1)
    print('#{} {}'.format(tc+1,max(w_dic.values())))
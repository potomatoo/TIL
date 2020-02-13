import sys
sys.stdin = open('./input/input_4873.txt','r')

TC = int(input())
for tc in range(TC):
    word = input()
    words = []
    for i in range(len(word)):
        words.append(word[i])

    while True:
        Sum_ = 0
        for i in range(len(words)-1):
            if words[i] == words[i+1]:
                del words[i]
                del words[i]
                Sum_ = 1
                break
        if Sum_ == 0:
            break
    print('#{} {}'.format(tc+1,len(words)))

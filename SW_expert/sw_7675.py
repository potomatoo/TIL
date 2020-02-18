import sys
sys.stdin = open('./input/input_7675.txt','r')

def check_name(word):
    cnt = 0
    for i in range(len(word)):
        if i == 0 and ord('A') <= ord(word[i]) <= ord('Z'):
            cnt += 1
        elif i != 0 and ord('a') <= ord(word[i]) <= ord('z'):
            cnt += 1
    if len(word) != 0 and cnt == len(word):
        return True
    else:
        return False

TC = int(input())
for tc in range(TC):
    N = int(input())
    word = input()
    words = []
    one = ''
    for i in range(len(word)):
        if word[i] == '!' or word[i] == '.' or word[i] == '?':
            words.append(one)
            one = ''
        else:
            one += word[i]

    for y in range(len(words)):
        words[y] = words[y].split(' ')

    result = []
    for y in range(len(words)):
        cnt = 0
        for x in range(len(words[y])):
            if check_name(words[y][x]):
                cnt += 1
        result.append(cnt)
    print('#%d'%(tc+1), end= ' ')
    for i in range(len(result)):
        if i == len(result)-1:
            print(result[i])
        else:
            print(result[i], end=' ')


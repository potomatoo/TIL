import sys
sys.stdin = open('input_5356.txt','r')

TC = int(input())
for tc in range(TC):
    word_ls = []
    len_ls = []
    for _ in range(5):
        word = input()
        len_ls.append(len(word))
        word_ls.append(word)
    max_len = max(len_ls)

    for i in range(len(word_ls)):
        if len(word_ls[i]) != max_len:
            word_ls[i] += ' '*(max_len - len(word_ls[i]))
    print(word_ls)
    print('#%d'%(tc+1),end=' ')
    for x in range(max_len):
        for y in range(5):
            if word_ls[y][x] == ' ':
                continue
            print(word_ls[y][x],end='')
    print()
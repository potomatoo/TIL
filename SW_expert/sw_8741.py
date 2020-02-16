import sys
sys.stdin = open('./input/input_8741.txt','r')

TC = int(input())
for tc in range(TC):
    words = input().split()
    print('#%d'%(tc+1), end=' ')
    for i in range(len(words)):
        print(words[i][0].upper(),end='')
    print()

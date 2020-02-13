import sys
sys.stdin = open('./input/input_4864.txt','r')

TC = int(input())
a = 1
for tc in range(TC):
    str1 = input()
    str2 = input()
    if str1 in str2:
        print('#{} {}'.format(a, '1'))
    else:
        print('#{} {}'.format(a, '0'))
    a += 1
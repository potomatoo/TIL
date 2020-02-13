import sys
sys.stdin = open('./input/input_4828.txt','r')

TC = int(input())
for tc in range(TC):
    n = int(input())
    number_ls = list(map(int,input().split()))
    max_num = number_ls[0]
    min_num = number_ls[-1]
    for i in range(1, len(number_ls)):
        if number_ls[i] > max_num:
            max_num = number_ls[i]
    for i in range(len(number_ls)-1,-1,-1):
        if number_ls[i] < min_num:
            min_num = number_ls[i]
    result = max_num - min_num
    print('#{} {}'.format(tc+1, result))
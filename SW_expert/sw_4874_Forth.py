import sys
sys.stdin = open('./input/input_4874.txt','r')

TC = int(input())
for tc in range(TC):
    word = input().split()
    S = []
    result = 0
    try:
        for i in range(len(word)):
            if word[i] == '.':
                if len(S) > 1:
                    print('#{} error'.format(tc+1))
                else:
                    print('#{} {}'.format(tc+1, int(S[0])))
                break
            elif word[i] == '+':
                result = S[-2] + S[-1]
                S.pop()
                S.pop()
                S.append(result)
            elif word[i] == '-':
                result = S[-2] - S[-1]
                S.pop()
                S.pop()
                S.append(result)
            elif word[i] == '*':
                result = S[-2] * S[-1]
                S.pop()
                S.pop()
                S.append(result)
            elif word[i] == '/':
                result = S[-2] / S[-1]
                S.pop()
                S.pop()
                S.append(result)
            else:
                S.append(int(word[i]))

    except IndexError:
        print('#{} error'.format(tc+1))




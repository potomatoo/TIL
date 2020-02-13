import sys
sys.stdin = open('./input/input_4866.txt','r')

TC = int(input())
for tc in range(TC):
    words = input()
    S = []
    for i in range(len(words)):
        if words[i] == '(':
            S.append('(')
        if words[i] == '{':
            S.append('{')
        if words[i] == ')':
            if S == []:
                S.append(')')
                break
            elif S.pop() == '{':
                break
        if words[i] == '}':
            if S == []:
                S.append('}')
                break
            elif S.pop() == '(':
                break

    if not S:
        print('#{} {}'.format(tc+1, 1))
    else:
        print('#{} {}'.format(tc+1, 0))

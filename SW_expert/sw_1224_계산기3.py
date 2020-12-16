import sys
sys.stdin = open('./input/input_1224.txt','r')

N = int(input())
cal = input()
backup = ''
S = []

for i in range(N):
    print(S)
    if cal[i] == '(':
        S.append(cal[i])

    elif cal[i] == '+' and S[-1] == '*':
        backup += cal[i]

    elif cal[i] == '+' and S[-1] == '/':
        backup += cal[i]

    elif cal[i] == '-' and S[-1] == '*':
        backup += cal[i]

    elif cal[i] == '-' and S[-1] == '/':
        backup += cal[i]

    elif cal[i] == '*' and S[-1] == '+':
        S.append(cal[i])

    elif cal[i] == '*' and S[-1] == '-':
        S.append(cal[i])

    elif cal[i] == '/' and S[-1] == '+':
        S.append(cal[i])

    elif cal[i] == '/' and S[-1] == '-':
        S.append(cal[i])

    elif cal[i] == '*' and S[-1] == '/':
        v = S.pop()
        backup += v
        S.append(cal[i])

    elif cal[i] == '*' and S[-1] == '*':
        v = S.pop()
        backup += v
        S.append(cal[i])

    elif cal[i] == '/' and S[-1] == '/':
        v = S.pop()
        backup += v
        S.append(cal[i])

    elif cal[i] == '/' and S[-1] == '*':
        v = S.pop()
        backup += v
        S.append(cal[i])

    elif cal[i] == ')':
        while True:
            if S[-1] == '(':
                S.pop()
                break
            v = S.pop()
            backup += v
    else:
        backup += cal[i]
print(S)
print(backup)
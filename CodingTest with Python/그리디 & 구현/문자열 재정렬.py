'''
알파벳 대문자와 숫자(0~9)로만 구성된 문자열이 입력으로 주어집니다.
이때 모든 알파벡을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 어어서 출력합니다.
'''

S = input()
alpha = []
value = 0
for i in range(len(S)):
    if S[i].isalpha():
        alpha.append(S[i])
    else:
        value += int(S[i])

alpha.sort()

answer = ''.join(alpha)
if value:
    answer += str(value)

print(answer)
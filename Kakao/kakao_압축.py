from string import ascii_uppercase

def solution(msg):
    answer = []
    alphabet = list(ascii_uppercase)
    dic = dict()

    for i in range(1, 27):
        dic[alphabet[i-1]] = i

    visit = [0 for _ in range(len(msg))]

    dic_idx = 27

    for i in range(len(msg)):
        if visit[i]:
            continue
        for j in range(i, len(msg)):
            check = msg[i:j+1]
            if check in dic:
                if j == len(msg)-1:
                    answer.append(dic[check])
                    return answer
                visit[j] = 1
            if check not in dic:
                dic[check] = dic_idx
                dic_idx += 1
                check = check[:-1]
                answer.append(dic[check])
                break


print(solution("ABABABABABABABAB"))
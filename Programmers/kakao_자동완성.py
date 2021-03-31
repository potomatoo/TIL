# 실패!

def solution(words):
    answer = 0
    for i in range(len(words)):
        mid_word = ""
        flag = False
        for j in range(len(words[i])):
            mid_word += words[i][j]
            mid_check = 0
            for k in range(len(words)):
                if i == k:
                    continue
                if mid_check:
                    break
                if mid_word in words[k]:
                    mid_check += 1
            if not mid_check:
                answer += len(mid_word)
                flag = True
                break
        if not flag:
            answer += len(words[i])

    return answer

print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]))

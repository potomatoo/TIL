def solution(s):
    answer = []
    words = s[2:-2]
    words = words.split('},{')
    words.sort(key= lambda x:len(x))
    for word in words:
        k = word.split(',')
        for num in k:
            if int(num) not in answer:
                answer.append(int(num))
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
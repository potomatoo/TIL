def solution(s):

    for i in range(len(s)):
        for j in range(len(s), -1, -1):
            word = s[i:j]
            if len(word) == 1:
                break
            reverse_word = word[::-1]
            if word == reverse_word:
                return len(word)
    return 1
print(solution("abacde"))
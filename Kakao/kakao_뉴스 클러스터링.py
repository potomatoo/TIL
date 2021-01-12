def find_set(s):
    new_s = dict()
    for i in range(len(s)-1):
        check = s[i] + s[i+1]
        if check[0].isalpha() and check[1].isalpha():
            if check in new_s:
                new_s[check] += 1
            else:
                new_s[check] = 1
    return new_s

def union_set(s1, s2, plus_dic):
    for key, value in s1.items():
        if key in s2:
            plus_dic[key] = max(value, s2[key])
        else:
            plus_dic[key] = value
    return plus_dic

def subtract_set(s1, s2, subtract_dic):
    for key, value in s1.items():
        if key in s2:
            subtract_dic[key] = min(value, s2[key])
    return subtract_dic

def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()
    new_str1 = find_set(str1)
    new_str2 = find_set(str2)
    if not new_str1 and not new_str2:
        return 65536
    plus_dic = dict()
    plus_dic = union_set(new_str1, new_str2, plus_dic)
    plus_dic = union_set(new_str2, new_str1, plus_dic)
    subtract_dic = dict()
    subtract_dic = subtract_set(new_str1, new_str2, subtract_dic)
    plus_sum = sum(plus_dic.values())
    subtract_sum = sum(subtract_dic.values())
    answer = int((subtract_sum / plus_sum) * 65536)
    return answer

print(solution('FRANCE', 'french'))
print(solution('handshake', 'shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))
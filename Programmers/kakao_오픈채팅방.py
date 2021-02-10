def solution(record):
    answer = []
    user_dic = dict()
    name_save = []
    behavior_save = []
    for i in range(len(record)):
        one = record[i].split()
        if one[0] == "Enter":
            user_dic[one[1]] = one[2]
            name_save.append(one[1])
            behavior_save.append('님이 들어왔습니다.')
        elif one[0] == "Leave":
            name_save.append(one[1])
            behavior_save.append('님이 나갔습니다.')
        elif one[0] == "Change":
            user_dic[one[1]] = one[2]
    for i in range(len(name_save)):
        answer.append(user_dic[name_save[i]] + behavior_save[i])
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
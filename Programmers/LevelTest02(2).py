def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        now_index = -1
        flag = True
        for i in range(len(skill_tree)):
            if skill_tree[i] not in skill:
                continue
            if skill.index(skill_tree[i]) != now_index+1:
                flag = False
                break
            now_index = skill.index(skill_tree[i])
        if flag:
            answer += 1
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))



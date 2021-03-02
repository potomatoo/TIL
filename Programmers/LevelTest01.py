def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        check = []
        flag = True
        for i in range(len(skill_tree)):
            if skill_tree[i] not in skill:
                continue
            else:
                if not check:
                    if skill_tree[i] != skill[0]:
                        flag = False
                        break
                    check.append(skill_tree[i])
                else:
                    if skill.index(check[-1]) + 1 != skill.index(skill_tree[i]):
                        flag = False
                        break
                    else:
                        check.append(skill_tree[i])

        if flag:
            answer += 1

    return answer

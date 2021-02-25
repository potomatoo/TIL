language_dic = {
    'cpp': 0,
    'java': 0,
    'python': 0
}

field_dic = {
    'backend': 0,
    'frontend': 0,
}

level_dic = {
    'junior': 0,
    'senior': 0
}

food_dic = {
    'chicken': 0,
    'pizza': 0
}
def solution(info, query):
    answer = []
    query_ls = []
    for i in range(len(info)):
        info_ls = info[i].split()
        language_dic[info_ls[0]] += 1
        field_dic[info_ls[0]] += 1
        level_dic[info_ls[0]] += 1
        food_dic[info_ls[0]] += 1
    for i in range(len(query)):
        mid_query = query[i].split(' and ')
        remain = mid_query[3].split()
        mid_query = mid_query[:3]
        for j in range(2):
            mid_query.append(remain[j])
        query_ls.append(mid_query)
    print(query_ls)
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
               , ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))


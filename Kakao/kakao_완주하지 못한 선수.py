# def solution(participant, completion):
#     people = dict()
#     check = dict()
#     for p in participant:
#         if p in people:
#             people[p] += 1
#         else:
#             people[p] = 0
#     for p in completion:
#         if p in check:
#             check[p] += 1
#         else:
#             check[p] = 0
#     for p in people:
#         if p not in check:
#             return p
#         if people[p] != check[p]:
#             return p


import collections

def solution(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    print(a, b)
    answer = a - b

    print(answer)
    return list(answer.keys())[0]

print(solution(['marina', 'josipa', 'marina', 'vinko', 'filipa'], ['josipa', 'filipa', 'marina']))

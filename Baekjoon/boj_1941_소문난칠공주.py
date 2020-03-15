from _collections import deque

sit = []
for y in range(5):
    sit.append(input())

sit_nums = []
k = 1

Q = deque()
visit = [[0 for _ in range(5)] for _ in range(5)]


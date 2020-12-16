# def permutation(arr):
#     result = [arr[:]]
#     c = [0] * len(arr)
#     i = 0
#     while i < len(arr):
#         if c[i] < i:
#             if i % 2 == 0:
#                 arr[0], arr[i] = arr[i], arr[0]
#             else:
#                 arr[c[i]], arr[i] = arr[i], arr[c[i]]
#             result.append(arr[:])
#             c[i] += 1
#             i = 0
#         else:
#             c[i] = 0
#             i += 1
#     return result
#
# def Cal(ls, plus, minus, multi, div):
#     c = []
#     for y in range(len(ls)):
#         cal = ls[y][0]
#         for x in range(1, len(ls[y])):
#             if 1 <= x <= plus:
#                 cal += ls[y][x]
#             if plus < x <= plus + minus:
#                 cal -= ls[y][x]
#             if plus + minus < x <= plus + minus + multi:
#                 cal *= ls[y][x]
#             if plus + minus + multi < x <= plus + minus + multi + div:
#                 if cal < 0:
#                     cal = -1*((-1*cal) // ls[y][x])
#                 else:
#                     cal = cal // ls[y][x]
#         c.append(cal)
#     return c
#
# N = int(input())
# num = list(map(int,input().split()))
# plus, minus, multi, div = map(int,input().split())
# ls = permutation(num)
# print(max(Cal(ls, plus, minus, multi, div)))
# print(min(Cal(ls, plus, minus, multi, div)))
def Plus(a, b):
    return a + b
a = 3
b = 4
for i in range(2):
    Plus(a, b)
    
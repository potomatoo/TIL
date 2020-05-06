import sys
sys.stdin = open('./input/input_2819.txt','r')

def dfs(y,x):
    global nums
    if len(nums) == 7:
        order.add(nums)
    else:
        for i in range(4):
            ty = y + dy[i]
            tx = x + dx[i]
            if ty < 0 or tx < 0 or ty >= 4 or tx >= 4:
                continue
            nums += str(g_map[ty][tx])
            dfs(ty,tx)
            nums = nums[:-1]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
TC = int(input())
for tc in range(TC):
    g_map = []
    for _ in range(4):
        g_map.append(list(map(int,input().split())))
    nums = ''
    order = set()
    for y in range(4):
        for x in range(4):
            dfs(y,x)
    print('#{} {}'.format(tc+1,len(order)))
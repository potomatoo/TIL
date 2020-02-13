# import sys
# sys.stdin = open('./input/input_1493.txt','r')

TC = int(input())
for tc in range(TC):
    p, q = map(int,input().split())
    p_sum, q_sum = 0, 0
    p_plus, q_plus = 1, 1
    p_cnt, q_cnt = 0, 0
    p_line, p_idx, q_line, q_idx = 0, 0, 0, 0
    while True:
        if p_sum > p:
            p_line, p_idx = p_cnt, p - (p_sum - p_cnt)
            break
        if p_sum == p:
            p_line, p_idx = p_cnt, p_cnt
            break
        p_sum += p_plus
        p_plus += 1
        p_cnt += 1

    while True:
        if q_sum > q:
            q_line, q_idx = q_cnt, q - (q_sum - q_cnt)
            break
        if q_sum == q:
            q_line, q_idx = q_cnt, q_cnt
            break
        q_sum += q_plus
        q_plus += 1
        q_cnt += 1

    p_x, p_y = p_idx, p_line - p_idx + 1
    q_x, q_y = q_idx, q_line - q_idx + 1
    result_x = p_x + q_x
    result_y = p_y + q_y

    result_line, result_idx = result_y + result_x - 1, result_x

    result = 0
    for i in range(1, result_line):
        result += i
    result = result + result_idx
    print('#{} {}'.format(tc+1, result))

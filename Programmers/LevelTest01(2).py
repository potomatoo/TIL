def solution(numbers, hand):
    answer = ''
    loc_dic = dict()
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9'],
        ['*', '0', '#']
    ]
    for y in range(4):
        for x in range(3):
            loc_dic[board[y][x]] = [y, x]

    right = '#'
    left = '*'
    for number in numbers:
        if number in [1, 4, 7]:
            left = str(number)
            answer += 'L'
        elif number in [3, 6, 9]:
            right = str(number)
            answer += 'R'
        else:
            right_gap = abs(loc_dic[right][0] - loc_dic[str(number)][0]) + abs(loc_dic[right][1] - loc_dic[str(number)][1])
            left_gap = abs(loc_dic[left][0] - loc_dic[str(number)][0]) + abs(loc_dic[left][1] - loc_dic[str(number)][1])
            if right_gap < left_gap:
                right = str(number)
                answer += 'R'
            elif right_gap > left_gap:
                left = str(number)
                answer += 'L'
            else:
                if hand == 'right':
                    right = str(number)
                    answer += 'R'
                else:
                    left = str(number)
                    answer += 'L'

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right'))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)

    while truck_weights:
        if sum(bridge)+truck_weights[0] <= weight:
            if bridge[-1] != 0:
                bridge.rotate(-1)
            bridge[-1] = truck_weights[0]
            truck_weights.pop(0)
            answer += 1
        else:
            while True:
                if bridge[0] != 0:
                    break
                bridge.rotate(-1)
                answer += 1
            if bridge[0] != 0:
                bridge[0] = 0
                bridge.rotate(-1)
                if sum(bridge)+truck_weights[0] <= weight:
                    if bridge[-1] != 0:
                        bridge.rotate(-1)
                    bridge[-1] = truck_weights[0]
                    truck_weights.pop(0)
                answer += 1

    while True:
        if sum(bridge) == 0:
            break
        if bridge[0] != 0:
            bridge[0] = 0

        bridge.rotate(-1)
        answer += 1

    return answer

print(solution(1, 2, [1, 1, 1]))
print(solution(1,1, [1,1,1]))
print(solution(4, 2, [1,1,1,1]))
print(solution(3, 3, [1, 1, 1]))
print(solution(3, 1, [1,1,1]))
print(solution(5, 5, [1,1,1,1,1,2,2]))
print(solution(7, 7, [1,1,1,1,1,3,3]))
print(solution(5, 5, [1,1,1,1,1,2,2,2,2]))
print(solution(5, 5, [2,2,2,2,1,1,1,1,1]))


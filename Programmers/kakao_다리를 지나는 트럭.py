bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

from _collections import deque

def solution(bridge_length, weight, truck_weights):
    def is_goal(bridge, bridge_sum):
        if bridge[0] != 0:
            complete.append(bridge[0])
            bridge_sum -= bridge.popleft()
            bridge.append(0)
            return bridge_sum
        return False
    time = 1
    bridge = deque(0 for _ in range(bridge_length))
    trucks = deque(truck_weights)
    flag = len(trucks)
    bridge[-1] = trucks[0]
    bridge_sum = sum(bridge)
    trucks.popleft()
    complete = []
    while True:
        if len(complete) == flag:
            break

        if trucks:
            ret = is_goal(bridge, bridge_sum)
            if type(ret) != type(1):
                if bridge_sum + trucks[0] <= weight:
                    bridge.rotate(-1)
                    bridge[-1] = trucks[0]
                    bridge_sum += trucks[0]
                    trucks.popleft()
                    time += 1
                    continue
                else:
                    bridge.rotate(-1)
                    time += 1
                    continue

            else:
                bridge_sum = ret
                if bridge_sum + trucks[0] <= weight:
                    bridge[-1] = trucks[0]
                    bridge_sum += trucks[0]
                    trucks.popleft()
                    time += 1
                    continue
                else:
                    time += 1
                    continue

        if not trucks and not is_goal(bridge, bridge_sum):
            bridge.rotate(-1)
            time += 1
            continue

        else:
            time += 1
            continue

    return time

print(solution(bridge_length, weight, truck_weights))
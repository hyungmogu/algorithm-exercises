# goal: solution 함수의 매개변수로 다리 길이 bridge_length, 다리가 견딜 수 있는 무게 weight,
# 트럭별 무게 truck_weights가 주어집니다. 이때 모든 트럭이 다리를 건너려면 최소 몇 초가 걸리는지
# return 하도록 solution 함수를 완성하세요.

# 제한 조건
#   - bridge_length는 1 이상 10,000 이하입니다.
#   - weight는 1 이상 10,000 이하입니다.
#   - truck_weights의 길이는 1 이상 10,000 이하입니다.
#   - 모든 트럭의 무게는 1 이상 weight 이하입니다.

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    time_elapsed = 0
    bridge_weight = 0
    N = len(truck_weights)

    # reformat trucks to following [[truck id, time spent moving across bridge]]
    # create a queue for waiting trucks
    trucks_queue = deque([[x,0] for x in truck_weights])
    in_progress = deque([])
    finished = deque([])

    # while
    while len(finished) != N:

        # if truck is done, then move to finished
        if is_alright_to_move_to_finish(in_progress, bridge_length):
            move_truck_to_finish(in_progress, finished)
            bridge_weight = remove_bridge_weight(finished, bridge_weight)

        # wait until more truck can be added
        # add more truck when free
        if is_alright_to_cross_bridge(trucks_queue, in_progress, bridge_weight, weight):
            move_truck_to_bridge(trucks_queue, in_progress)
            bridge_weight = add_bridge_weight(in_progress, bridge_weight)

        update_trucks_on_bridge(in_progress)
        time_elapsed += 1

    # once all trucks have moved to the end of bridge, return answer
    answer = time_elapsed
    return answer

def is_alright_to_cross_bridge(trucks_queue, in_progress, bridge_weight, weight):
    if len(trucks_queue) == 0:
        return False

    if bridge_weight + trucks_queue[0][0] > weight:
        return False

    if len(in_progress) > 0 and in_progress[-1][1] < 1:
        return False

    return True

def move_truck_to_bridge(trucks_queue, in_progress):
    if len(trucks_queue) == 0:
        return

    truck = trucks_queue.popleft()
    in_progress.append(truck)

def update_trucks_on_bridge(in_progress):
    for truck in in_progress:
        truck[1] += 1

def is_alright_to_move_to_finish(in_progress, bridge_length):
    if len(in_progress) == 0:
        return False

    if in_progress[0][1] < bridge_length:
        return False

    return True


def move_truck_to_finish(in_progress, finished):
    if len(in_progress) == 0:
        return
    truck = in_progress.popleft()
    truck[1] = 1
    finished.append(truck)

def add_bridge_weight(in_progress, bridge_weight):
    truck_weight = in_progress[-1][0]

    return bridge_weight + truck_weight

def remove_bridge_weight(finished, bridge_weight):
    truck_weight = finished[-1][0]

    return bridge_weight - truck_weight


if __name__ == "__main__":
    print(solution(2, 10, [7,4,5,6])) #8
    print(solution(100, 100, [10])) #101
    print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10])) #110
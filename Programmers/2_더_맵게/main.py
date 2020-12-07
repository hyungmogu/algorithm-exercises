# goal: Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution
# 함수를 작성해주세요.
#   - scoville의 길이는 2 이상 1,000,000 이하입니다.
#   - K는 0 이상 1,000,000,000 이하입니다.
#   - scoville의 원소는 각각 0 이상 1,000,000 이하입니다.
#   - 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 return 합니다.

import heapq

def solution(scoville, K):
    N = len(scoville)
    answer = 0

    heapq.heapify(scoville)

    i = 1
    while i < N:
        if scoville[i-1] < K:
            food_1 = heapq.heappop(scoville)
            food_2 = heapq.heappop(scoville)

            new_food_scoville = mix_food(food_1, food_2)
            heapq.heappush(scoville, new_food_scoville)

            N = len(scoville)
            answer += 1

        if N == 1 and scoville[0] <= K:
            return -1

        if scoville[0] > K:
            break

    return answer

def mix_food(food_1, food_2):
    lesser_spicy = min(food_1, food_2)
    more_spicy = max(food_1, food_2)

    return lesser_spicy + (more_spicy * 2)

if __name__ == "__main__":
    print(solution([1, 2, 3, 9, 10, 12], 7))
    print(solution([1,1], 2))
    print(solution([1,1], 4))
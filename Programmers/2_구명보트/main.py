# goal: 사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
# 모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   - 무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
#   - 각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
#   - 구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
#   - 구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

from collections import deque

def solution(people, limit):
    # sort people in increasing order
    N = len(people)
    people = deque(sorted(people, reverse=True))
    current_weight = 0
    count = 0

    while len(people) != 0:
        current_weight += people.popleft()
        is_full = False
        if len(people) == 0:
            count += 1
            break

        # while boat is not full
        while not is_full:
            small_weight = people[-1]

            if small_weight + current_weight <= limit:
                current_weight += small_weight
                people.pop()

                if len(people) == 0:
                    count += 1
                    current_weight = 0
                    is_full = True
            else:
                count += 1
                current_weight = 0
                is_full = True

    answer = count
    return answer

if __name__ == "__main__":
    print(solution([70], 100)) #1
    print(solution([70, 50, 80, 50], 100)) #3
    print(solution([70, 80, 50], 100)) #3
# Goal: 모든 사람이 심사를 받는데 걸리는 시간을 최소로 하라
#
# restrictions
#   - 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
#   - 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
#   - 심사관은 1명 이상 100,000명 이하입니다.

# test: 60 minutes
#   - 심사관 1: floor(60 / 7) -> 8
#   - 심시관 2: floor(60 / 10) -> 10
# More people can be analyzed

# time max - 60 minutes (upper bound)
# time min - 0 minutes

# test: 30 minutes
#   - 심사관 1: floor(30 / 7) -> 4
#   - 심사관 2: floor(30 / 10) -> 3
#   More people can be analyzed

# time max - 30 minutes (upper bound)
# time min - 0 minutes (lower bound)

# test: 15 minutes
#   - 심사관 1: floor(15 / 7) -> 2
#   - 심시관 2: floor(15 / 10) -> 1
#   Less people can be analyzed

# time max - 30 minutes (upper bound)
# time min - 15 minutes (lower bound)

# test: 27 ((30 + 15)/2 -> 27) minutes
#   - 심사관 1: floor(27 / 7) -> 3
#   - 심시관 2: floor(27 / 10) -> 2
#   Less number of people can be analyzed

# time max - 28 minutes (upper bound)
# time min - 27 minutes (lower bound)

# test: 28 ((27 + 28)/2 -> 27) minutes
#   - 심사관 1: floor(27 / 7) -> 3
#   - 심시관 2: floor(27 / 10) -> 2
#   Less number of people can be analyzed

# time max - 28 minutes (upper bound)
# time min - 27 minutes (lower bound)
import math

def solution(n, times):
    answer = 0
    # find maximum amount of time required
    upper_time= max(times) * n
    lower_time = 0

    # while upper_bound and lower_bound are not crossing
    while lower_time < upper_time:
        # calculate the middle
        number_of_people_analyzed = 0
        middle = math.floor((upper_time + lower_time) / 2)
        for time in times:
            number_of_people_analyzed += math.floor(middle / time)

        # if less people can be analyzed, then set lower bound to middle
        if number_of_people_analyzed < n:
            lower_time = middle + 1
        else:
            # if more people can be analyzed, then deacrease upper bound
            upper_time = middle

    answer = upper_time
    return answer

if __name__ == "__main__":
    print(solution(6, [1,1,1])) #2
    print(solution(6, [7,10])) #28
    print(solution(6, [10,7])) #28
    print(solution(6, [10]))
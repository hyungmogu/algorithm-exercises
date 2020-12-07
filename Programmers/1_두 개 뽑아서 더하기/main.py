# 문제를 이해한다
# goal: numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에
# 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - numbers의 길이는 2 이상 100 이하입니다.
#   - numbers의 모든 수는 0 이상 100 이하입니다.

def solution(numbers):
    N = len(numbers)
    answer = []
    result_set = set()

    # sort numbers
    numbers.sort()

    # for each number in numbers (number_1),
    i = 0
    while i < N:
        number_1 = numbers[i]
        # for each subsequent numbers (number_2),
        j = 0
        while j < N:
            if i == j:
                j += 1
                continue

            # add two numbers (number_1 + number_2)
            number_2 = numbers[j]

            # add to set
            result_set.add(number_1 + number_2)
            j += 1
        i += 1

    # convert to list
    # return list
    answer = list(result_set)
    answer.sort()
    return answer

if __name__ == "__main__":
    print(solution([2,1]))
    print(solution([2,1]))
    print(solution([2,1,3,4,1]))
    print(solution([5,0,2,7]))
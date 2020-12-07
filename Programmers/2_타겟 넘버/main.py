
# Goal:
# - N:  >= 2 and <= 20
# - numbers[i]: >= 1 and <= 50
# - target: >= 1 and <= 1000

def solution(numbers, target):
    answer = _solution(numbers[0], target, 1, numbers) + _solution(-numbers[0], target, 1, numbers)

    return answer

def _solution(value, target, index, numbers):
    if index == len(numbers):
        return 1 if value == target else 0

    count_left = _solution(value + numbers[index], target, index + 1, numbers)
    count_right = _solution(value - numbers[index], target, index + 1, numbers)

    return count_left + count_right

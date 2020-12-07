# goal: 각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는
# 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - numbers는 길이 1 이상 7 이하인 문자열입니다.
#   - numbers는 0~9까지 숫자만으로 이루어져 있습니다.
#   - 013은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

from itertools import permutations
import math

def solution(numbers):
    answer = 0
    N = len(numbers)
    numbers_set = set()

    # split numbers to array of digits
    if numbers == "":
        return 0

    i = 0
    while i < N:
        perms = permutations(numbers, (i+1))
        for number in perms:
            number = int("".join(number))

            if not is_prime_number(number):
                continue

            numbers_set.add(number)
        i += 1


    # calculate length of combination of words
    return len(numbers_set)

def is_prime_number(number):
    number = int(number)

    if number == 1 or number == 0:
        return False

    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True

# import math

# def solution(numbers):
#     answer = 0
#     N = len(numbers)
#     combinations = set()

#     # split numbers to array of digits
#     if numbers == "":
#         return 0

#     # use DFS to find all combination of words
#     _solution("", numbers, combinations, N)

#     print(combinations)

#     for combination in combinations:
#         if is_prime_number(int(combination)):
#             answer += 1

#     # calculate length of combination of words
#     return answer

# def _solution(combined_number, numbers, combinations, target_length):

#     # if combined word length matches target, add to set and return
#     if len(combined_number) == target_length:
#         return

#     # if not, continue to add combinations
#     # for each character in numbers
#     N = len(numbers)
#     i = 0
#     while i < N:
#         # pop it
#         number = numbers[i]
#         # add to combination
#         new_combined_number = str(int(combined_number + number))

#         combinations.add(new_combined_number)

#         # get reminaing numbers after pop
#         new_numbers = numbers[:i] + numbers[i+1:]
#         _solution(new_combined_number, new_numbers, combinations, target_length)

#         i += 1

# def is_prime_number(number):
#     number = int(number)

#     if number == 1 or number == 0:
#         return False

#     i = 2
#     while i <= number:
#         if number > 2 and number % 2 == 0:
#             return False

#         if number > 3 and number % 3 == 0:
#             return False

#         if not math.gcd(i, number) in [1, number]:
#             return False

#         i += 1

#     return True

if __name__ == "__main__":
    print(solution("17")) #3
    print(solution("011")) #2
    print(solution("")) #0
    print(solution("1")) #0
    print(solution("0")) #0
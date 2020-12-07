# goal: 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를
# 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
#   nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.

from itertools import combinations

def solution(nums):
    count = 0

    # get all combinations
    combinations_list = combinations(nums, 3)

    # for each combination,
    for comb in combinations_list:
        # add sum
        number = sum(comb)
        # if sum ends with 2 or 0 continue
        if number % 2 == 0:
            continue
        # otherwise, check for prime number
        if is_prime(number):
            # if so, add count
            count += 1

    # return count
    answer = count
    return answer

def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

if __name__ == "__main__":
    print(solution([1,2,3,4])) #1
    print(solution([1,2,7,6,4])) #4
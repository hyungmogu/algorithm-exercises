# goal: 자연수 n이 매개변수로 주어질 때, n의 다음 큰 숫자를 return 하는 solution 함수를 완성해주세요.

# 조건 1. n의 다음 큰 숫자는 n보다 큰 자연수 입니다.
# 조건 2. n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같습니다.
# 조건 3. n의 다음 큰 숫자는 조건 1, 2를 만족하는 수 중 가장 작은 수 입니다.

# 제한 사항
#   - n은 1,000,000 이하의 자연수 입니다.

# Example
#   1. 78 (1001110) (4 1's)
#       1) 79 - 1001111 (5 1's)
#       2) 80 - 1010000 (2 1's)
#       3) 81 - 1010001 (3 1's)
#       4) 82 - 1010010 (3 1's)
#       5) 83 - 1010011 (4 1's)

# pseudocode
#   1. convert n to binary number
#   2. count number of 1's in binary form of n
#   3. for each consecutive number,
#       3.1 convert to binary form and find number of 1's
#       3.2 if the number of 1's are equal, then return the consecutive number

from collections import deque

def solution(n):
    answer = 0

    # 1. convert n to binary number
    n_binary_list = convert_to_binary(n)

    # 2. count number of 1's in binary form of n
    count_n = sum(n_binary_list)
    # 3. for each consecutive number,
    i = n + 1
    while True:
        # 3.1 convert to binary form and find number of 1's
        i_binary_list = convert_to_binary(i)
        count_i = sum(i_binary_list)
        # 3.2 if the number of 1's are equal, then return the consecutive number
        if count_n == count_i:
            return i
        i += 1

    return answer

def convert_to_binary(n):
    binary_list = deque()

    while n != 0:
        binary_list.appendleft(n % 2)
        n = n // 2

    return list(binary_list)


if __name__ == "__main__":
    print(solution(78)) #83
    print(solution(15)) #23
    print(solution(1)) #2
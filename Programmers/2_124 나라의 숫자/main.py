# goal: 자연수 n이 매개변수로 주어질 때, n을 124 나라에서 사용하는 숫자로 바꾼 값을 return 하도록
# solution 함수를 완성해 주세요.

# 제한사항
#   - n은 500,000,000이하의 자연수 입니다.


from collections import deque

def solution(n):

    if n == 1 or n == 2:
        return str(n)

    strange_number = convert_from_decimal_to_strange(n)

    answer = strange_number

    return answer

def convert_from_decimal_to_strange(n):
    strange_list = ["4", "1", "2"]
    ternary_number = ''
    quotient = n

    while quotient != 0:
        remainder = quotient % 3
        quotient = quotient // 3 if remainder != 0 else (quotient // 3) - 1

        ternary_number = strange_list[remainder] + ternary_number

    return ternary_number

if __name__ == "__main__":
    print(solution(1)) #1
    print(solution(2)) #2
    print(solution(3)) #4
    print(solution(4)) #11
    # print(solution(27)) #224
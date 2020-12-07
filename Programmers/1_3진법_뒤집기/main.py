# goal: 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로
# 표현한 수를 return 하도록 solution 함수를 완성해주세요.
#   - n은 1 이상 100,000,000 이하인 자연수입니다.

def solution(n):

    # convert decimal to ternary
    ternary = convert_decimal_to_ternary(n)

    # reverse order of ternary
    ternary = ternary[::-1]

    # convert back from ternary to decimal
    answer = convert_ternary_to_decimal(ternary)

    # return answer
    return answer

def convert_decimal_to_ternary(n):
    ternary = ''
    quotient = n
    # while quotient is not 0
    while quotient != 0:
        # find modulo of number
        remainder = quotient % 3
        # add to variable ternary
        ternary = str(remainder) + ternary
        # update n with value integer division of n by 3
        quotient = quotient // 3

    return ternary


def convert_ternary_to_decimal(ternary):
    n = len(ternary) - 1
    total = 0
    i = n
    # while n is greater than equal to 0
    while i >= 0:
        # multiply each digit in ternary (starting from the left) by i
        # add to total
        total +=  (int(ternary[n - i]) * 3**(i))
        # decrement
        i -= 1

    return total

if __name__ == "__main__":
    print(solution(0))
    print(solution(1))
    print(solution(45)) #7
    print(solution(125)) #229
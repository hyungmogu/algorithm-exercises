# goal: 가로의 길이 W와 세로의 길이 H가 주어질 때, 사용할 수 있는 정사각형의 개수를 구하는 solution
# 함수를 완성해 주세요.

# 제한사항
#   - W, H : 1억 이하의 자연수

import math

def solution(w,h):
    answer = 1

    # if it's not a square
    number_of_squares_in_a_diagonal = get_number_of_squares_in_a_diagonal(w, h)
    total_squares = w * h

    answer = total_squares - number_of_squares_in_a_diagonal
    return answer


def get_number_of_squares_in_a_diagonal(width, height):

    gcd = math.gcd(width, height)

    d_width = width / gcd
    d_height = height / gcd

    return int((d_width + d_height - 1) * gcd)


if __name__ == "__main__":
    print(solution(8, 12)) #80
# goal: 순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열
# hand가 매개변수로 주어질 때, 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된
# 문자열 형태로 return 하도록 solution 함수를 완성해주세요.
#
#   - 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
#   - 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
#   - 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
#   - 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
#       - 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# 제한사항
#   - numbers 배열의 크기는 1 이상 1,000 이하입니다.
#   - numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
#   - hand는 "left" 또는 "right" 입니다.
#   - "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
#   - 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

import math

def solution(numbers, hand):
    answer = ''

    left_hand = "*"
    right_hand = "#"

    # for each number
    for number in numbers:
        # find which thumb is pressed for the number
        hand_used = get_pressed_hand(left_hand, right_hand, str(number), hand)
        # update current hand position
        if hand_used == "L":
            left_hand = str(number)
        else:
            right_hand = str(number)

        # concat to answer
        answer += hand_used

    # return answer
    return answer

def get_pressed_hand(left_hand, right_hand, number, hand):

    button_positions = {"1":[0,0],"2":[0,1],"3":[0,2],
                        "4":[1,0],"5":[1,1],"6":[1,2],
                        "7":[2,0],"8":[2,1],"9":[2,2],
                        "*":[3,0],"0":[3,1],"#":[3,2]}

    if number in ["1","4","7"]:
        return "L"
    elif number in ["3","6","9"]:
        return "R"
    else:
        position_number = button_positions[number]
        position_left_hand = button_positions[left_hand]
        position_right_hand = button_positions[right_hand]

        distance_to_number_left_hand = get_distance(position_left_hand, position_number)
        distance_to_number_right_hand = get_distance(position_right_hand, position_number)

        if distance_to_number_left_hand == distance_to_number_right_hand:
            return "L" if hand == "left" else "R"
        else:
            return "L" if distance_to_number_left_hand < distance_to_number_right_hand else "R"

def get_distance(position_1, position_2):
    distance_horizontal = abs(position_1[1] - position_2[1])
    distance_vertical = abs(position_1[0] - position_2[0])

    distance_total = distance_horizontal + distance_vertical

    return distance_total

if __name__ == "__main__":
    assert(solution([5], "right") == "R")
    assert(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right") == "LRLLLRLLRRL")
    assert(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left") == "LRLLRRLLLRR")
    assert(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right") == "LLRLLRLLRL")
# goal: 만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을
# return 하도록 solution 함수를 만드세요

# 제한 사항
#   - name은 알파벳 대문자로만 이루어져 있습니다.
#   - name의 길이는 1 이상 20 이하입니다.

# Example
#   - JAZ --> 56
#       - [9]: 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
#       - [10]: 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
#       - [11]: 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
#           - 따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
#   - JAN --> 23
#       - [9]: 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
#       - [10]: 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
#       - [23]: 마지막 위치에서 조이스틱을 아래로 13번 조작하여 N를 완성합니다.
#           - 따라서 23번 이동시켜 "JAN"를 만들 수 있고, 이때가 최소 이동입니다.

# pattern
#   - Always choose directions closest to current cursor

# Detail
#   - JAZ
#       1. AAA -> Check distance between A and J (9 by up 17 by down) --> choose up by 9 --> add to total (9)
#          ^
#          JAZ
#          *
#       2. JAA
#          ^
#          JAZ
#          *
#       3. JAA -> Next is A --> skip
#          ^
#          JAZ
#           *
#       4. JAA -> Next is Z --> Calculate  distance between left and right cursur (2 by right, 1 by left) --> move left by 1 --> add tototal (10)
#          ^
#          JAZ
#            *
#       5. JAA ->Check distance between A and Z (25 by up 1 by down) --> choose down by 1 --> add to total (11)
#            ^
#          JAZ
#            *
#       6. JAZ
#            ^
#          JAZ
#            *

# BBBBAAAABA
#       1. AAAAAAAAAA -> Check distance between A and B (1 by up - by down) --> choose up by 1 --> add to total (1)
#          ^
#          BBBBAAAABA
#          *
#       2. BAAAAAAAAA
#          ^
#          BBBBAAAABA
#          *
#       3. BAAAAAAAAA -> Calculate distance between left and right cursur (1 by right, - by left) --> move right by 1 --> add tototal (2)
#          ^
#          BBBBAAAABA
#           *
#       4. BAAAAAAAAA -> Check distance between A and B (1 by up - by down) --> choose up by 1 --> add to total (3)
#           ^
#          BBBBAAAABA
#           *
#       5. BBAAAAAAAA
#           ^
#          BBBBAAAABA
#           *
#       6. BBAAAAAAAA
#           ^
#          BBBBAAAABA -> Calculate distance between left and right cursur (1 by right, - by left) --> move right by 1 --> add tototal (4)
#            *
#       7. BBAAAAAAAA
#            ^
#          BBBBAAAABA -> Check distance between A and B (1 by up - by down) --> choose up by 1 --> add to total (5)
#            *
#       8. BBBAAAAAAA
#            ^
#          BBBBAAAABA
#            *
#       9. BBBAAAAAAA -> Calculate distance between left and right cursur (1 by right, - by left) --> move right by 1 --> add tototal (6)
#            ^
#          BBBBAAAABA
#             *
#       9. BBBAAAAAAA --> Check distance between A and B (1 by up - by down) --> choose up by 1 --> add to total (7)
#             ^
#          BBBBAAAABA
#             *
#       10.BBBBAAAAAA
#             ^
#          BBBBAAAABA
#             *
#       11.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#              *
#       12.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#              *
#       13.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#              *
#       14.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#               *
#       15.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#                *
#       16.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#                 *
#       17.BBBBAAAAAA --> letter is A --> skip
#             ^
#          BBBBAAAABA
#                 *
#       18.BBBBAAAAAA --> Check distance between A and B (1 by up - by down) --> choose up by 1 --> add to total (7)
#             ^
#          BBBBAAAABA
#                  *

# cases
#   If length of name is 1
#   If length of name is not 1
    #   If index == 0
    #   If index != 0

    #   Vertical
    #       1. if the current letter and target letter are the same
    #       2. if the current letter and target letter are not the same
    #           2.1 if is closer moving up
    #           2.2 if is closer moving down
    #   Horizontal
    #       1. if closer by moving left
    #       1. if closer by moving right

def solution(name):
    my_index = 0
    my_name = ["A"] * len(name)
    completed_count = 0
    total_moves = 0
    N = len(name)

    i = 0
    while completed_count < N:
        letter = name[i]

        total_moves += move_vertical(letter)
        my_name[i] = letter

        if "".join(my_name) == name:
            break

        horizontal_move_amt, i = move_horizontal(i, name, my_name, N)
        total_moves += horizontal_move_amt


    answer = total_moves
    return answer

def move_vertical(letter):
    # find which has closer distance
    distance_up = ord(letter) - ord("A")
    distance_down = ord("Z") - ord(letter) + 1

    return distance_up if distance_up < distance_down else distance_down

def move_horizontal(i, name, my_name, N):
    # find closest non-filled letter to left and its index
    i_left = i - 1
    distance_left = 1
    while distance_left % N != 0:
        if name[i_left] != my_name[i_left]:
            break
        i_left -= 1
        distance_left += 1

    # find closest non-filled letter to right and its index
    i_right = i + 1
    distance_right = 1
    while distance_right % N != 0:
        if name[i_right % N] != my_name[i_right % N]:
            break
        i_right += 1
        distance_right += 1

    distance = distance_left if distance_left < distance_right else distance_right
    index = i_left if distance_left < distance_right else i_right
    return distance, index

if __name__ == "__main__":
    print(solution("JAZ")) #11
    print(solution("J")) #9
    print(solution("JEROEN")) #56
    print(solution("JAN")) #23
    print(solution("ABAAAAAAABA")) #6
    print(solution("ZZZ")) #5
    print(solution("BAB")) #3
    print(solution("BBBBAAAABA")) #13
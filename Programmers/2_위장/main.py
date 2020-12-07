# goal: 스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를
# return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   - clothes의 각 행은 [의상의 이름, 의상의 종류]로 이루어져 있습니다.
#   - 스파이가 가진 의상의 수는 1개 이상 30개 이하입니다.
#   - 같은 이름을 가진 의상은 존재하지 않습니다.
#   - clothes의 모든 원소는 문자열로 이루어져 있습니다.
#   - 모든 문자열의 길이는 1 이상 20 이하인 자연수이고 알파벳 소문자 또는 '_' 로만 이루어져 있습니다.
#   - 스파이는 하루에 최소 한 개의 의상은 입습니다.



def solution(clothes):
    answer = 1
    types_hash = {}

    if len(clothes) == 0:
        return 0

    if len(clothes) == 1:
        return 1

    # find number of types
    for clothe in clothes:
        print(clothe)
        clothe_type = clothe[1]
        if clothe_type not in types_hash:
            types_hash[clothe_type] = 1
        else:
            types_hash[clothe_type] += 1

    for key in types_hash:
        answer *= (types_hash[key] + 1)

    answer = answer - 1
    return answer

# from itertools import combinations

# def solution(clothes):
#     answer = 0
#     # find number of types
#     number_of_types = len(set([x[1] for x in clothes]))
#     clothes_set = set()

#     i = 1
#     while i <= number_of_types:
#         # get permutations of the clothes
#         combs = combinations(clothes, i)

#         # filter combination of same type
#         for combination in combs:
#             if not has_the_same_kind_of_clothes(combination):
#                 answer += 1

#         i += 1
#     # return total number of combinations

#     return answer

# def has_the_same_kind_of_clothes(combination):
#     i = 0

#     if len(combination) == 1:
#         return False

#     clothe_types_set = set([x[1] for x in combination])
#     if len(clothe_types_set) == len(combination):
#         return False

#     return True

if __name__ == "__main__":
    # print(solution([])) #0
    # print(solution([["yellow_hat", "headgear"]])) #1
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) #5
    # print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) #3

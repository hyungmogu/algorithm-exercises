# goal: 선행 스킬 순서 skill과 유저들이 만든 스킬트리1를 담은 배열 skill_trees가 매개변수로 주어질
# 때, 가능한 스킬트리 개수를 return 하는 solution 함수를 작성해주세요.

#제한 조건
    # - 스킬은 알파벳 대문자로 표기하며, 모든 문자열은 알파벳 대문자로만 이루어져 있습니다.
    # - 스킬 순서와 스킬트리는 문자열로 표기합니다.
        # - 예를 들어, C → B → D 라면 CBD로 표기합니다
    # - 선행 스킬 순서 skill의 길이는 1 이상 26 이하이며, 스킬은 중복해 주어지지 않습니다.
    # - skill_trees는 길이 1 이상 20 이하인 배열입니다.
    # - skill_trees의 원소는 스킬을 나타내는 문자열입니다.
    # - skill_trees의 원소는 길이가 2 이상 26 이하인 문자열이며, 스킬이 중복해 주어지지 않습니다.

import sys

def solution(skill, skill_trees):
    answer = 0

    # for each skill_tree in skill trees
    for skill_tree in skill_trees:
        # if skill is not valid in skill_tree, continue
        if not is_valid(skill, skill_tree):
            continue
        # else, add count
        answer += 1

    # return answer

    return answer

def is_valid(skill, skill_tree):
    order = 1
    N_skill_tree = len(skill_tree)
    N_skill = len(skill)
    skill_order_by_name = {}

    for skill_name in skill:
        skill_order_by_name[skill_name] = sys.maxsize

    i = 0
    while i < N_skill_tree:
        skill_name = skill_tree[i]
        if skill_name in skill_order_by_name:
            skill_order_by_name[skill_name] = i

        i+=1

    if N_skill == 1:
        skill_name = skill[0]
        return True if skill_order_by_name[skill_name] <= sys.maxsize else False

    j = 1
    while j < N_skill:
        skill_name_prev = skill[j-1]
        skill_name_current = skill[j]

        if skill_order_by_name[skill_name_prev] > skill_order_by_name[skill_name_current]:
            return False

        j += 1
    return True

if __name__ == "__main__":
    print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])) #2
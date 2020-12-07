# goal: 전체 학생의 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온
# 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때, 체육수업을 들을 수 있는 학생의 최댓값을
# return 하도록 solution 함수를 작성해주세요.

#  Restrictions
# - 전체 학생의 수는 2명 이상 30명 이하입니다.
# - 체육복을 도난당한 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# - 여벌의 체육복을 가져온 학생의 수는 1명 이상 n명 이하이고 중복되는 번호는 없습니다.
# - 여벌 체육복이 있는 학생만 다른 학생에게 체육복을 빌려줄 수 있습니다.
# - x 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.

def solution(n, lost, reserve):
    answer = 0

    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)

    for student_number in set_reserve:
        if (student_number - 1) in set_lost:
            set_lost.remove(student_number - 1)
        elif (student_number + 1) in set_lost:
            set_lost.remove(student_number + 1)

    answer = n - len(set_lost)
    return answer

if __name__ == "__main__":
    print(solution(5, [2,3], [2, 4]))
    print(solution(5, [2,4], [1, 3, 5]))
    print(solution(5, [2,4], [3]))
    print(solution(3, [3], [1]))
    print(solution(5, [7,8,9], [1, 3, 5]))
    print(solution(5, [7,5,3], [4, 6, 8]))
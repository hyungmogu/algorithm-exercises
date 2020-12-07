# goal: 어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이
# 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요
#
# 제한 사항
#   - 과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
#   - 논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

def solution(citations):
    N = len(citations)

    if N == 0:
        return 0

    citations = sorted(citations)

    h_index = citations[-1]

    while h_index >= 0:
        j = N - 1
        count_above_or_equal_h_index = 0

        while j >= 0:
            if citations[j] >= h_index:
                count_above_or_equal_h_index = count_above_or_equal_h_index + 1

            count_less_or_equal_h_index = N - count_above_or_equal_h_index

            if ((count_above_or_equal_h_index >= h_index) and
            (count_less_or_equal_h_index <= h_index)):
                answer = h_index
                return answer
            j -= 1
        h_index -= 1

    return 0

if __name__ == "__main__":
    print(solution([])) #0
    print(solution([1])) #1
    print(solution([3, 0, 6, 1, 5])) #3
    print(solution([1, 1, 1, 1, 1])) #1
    print(solution([5,5,5,5])) #4
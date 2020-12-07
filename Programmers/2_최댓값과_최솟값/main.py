# goal: str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 문자열을 반환하는
# 함수, solution을 완성하세요.

def solution(s):
    if s == "":
        return ""

    s_list = [int(x) for x in s.split(" ")]
    min_value = min(s_list)
    max_value = max(s_list)

    answer = "{} {}".format(min_value, max_value)
    return answer

if __name__ == "__main__":
    print(solution("")) #
    print(solution("1 2 3 4")) #1 4
    print(solution("-1 -2 -3 -4")) #-4 -1
    print(solution("-1 -1")) #-1 1
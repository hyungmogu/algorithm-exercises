# goal: 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

def solution(s):
    answer = ''
    N = len(s)

    if N < 3:
        return s

    middle = N//2
    if N % 2 == 1:
        answer = s[middle]
    else:
        answer = s[middle-1] + s[middle]

    return answer
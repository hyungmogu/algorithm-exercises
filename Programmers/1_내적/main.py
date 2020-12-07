# goal: 길이가 같은 두 1차원 정수 배열 a, b가 매개변수로 주어집니다. a와 b의 내적을 return 하도록
# solution 함수를 완성해주세요.

def solution(a, b):
    N = len(a)
    i = 0
    answer = 0
    while i < N:
        answer += a[i] * b[i]
        i += 1

    return answer


# goal: 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수,
# solution을 완성해 주세요.

# 제한사항
#   - * n은 1이상, 100000이하인 자연수입니다.

def solution(n):
    answer = 0
    hash = {0: 0, 1: 1}

    for i in range(n+1):

        if i == 0 or i == 1:
            continue

        hash[i] = hash[i-1] + hash[i-2]

    return hash[n] % 1234567

if __name__ == "__main__":
    print(solution(3)) #2
    print(solution(5)) #5
    print(solution(100000)) #
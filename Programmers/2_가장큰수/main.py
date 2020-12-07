# Goal: 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.
#   - numbers의 길이는 1 이상 100,000 이하입니다.
#   - numbers의 원소는 0 이상 1,000 이하입니다.
#   - 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다

def solution(numbers):
    answer = ''
    numbers = [str(x) for x in numbers]
    numbers.sort(key=lambda e: e * 3, reverse=True)
    answer = ''.join(numbers)

    return str(int(answer))

if __name__ == "__main__":
    print(solution([40,403])) #40403
    print(solution([10,101])) #10110
    print(solution([1,11, 111, 1111])) #1111111111
    print(solution([0,0, 0, 0])) #0
    print(solution([121, 12]))
    print(solution([0, 0, 1, 10, 1000]))
    print(solution([1, 10, 1000]))
    print(solution([1, 10, 110]))
    print(solution([6, 10, 2]))
    print(solution([6]))
    print(solution([0,1]))
    print(solution([8,886,884]))
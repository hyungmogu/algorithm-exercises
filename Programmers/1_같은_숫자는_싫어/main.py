#goal: 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.
#
# 제한사항
#   - 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다. 예를 들면,
#   - 배열 arr의 크기 : 1,000,000 이하의 자연수
#   - 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

def solution(arr):
    N = len(arr)
    answer = []

    if N == 1 or N == 0:
        return arr

    answer.append(arr[0])
    current_number = arr[0]

    i = 0
    while i < N:
        # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        if arr[i] != current_number:
            answer.append(arr[i])
            current_number = arr[i]

        i += 1
    return answer

if __name__ == "__main__":
    print(solution([1,1,3,3,0,1,1]))
    print(solution([4,4,4,3,3]))
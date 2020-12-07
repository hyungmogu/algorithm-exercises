# Goal: 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발
# 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 하도록
# solution 함수를 완성하세요.
#   - 작업의 개수(progresses, speeds배열의 길이)는 100개 이하입니다.
#   - 작업 진도는 100 미만의 자연수입니다.
#   - 작업 속도는 100 이하의 자연수입니다.
#   - 배포는 하루에 한 번만 할 수 있으며, 하루의 끝에 이루어진다고 가정합니다. 예를 들어 진도율이 95%인 작업의 개발 속도가 하루에 4%라면 배포는 2일 뒤에 이루어집니다.

def solution(progresses, speeds):
    answer = []
    count = 0
    while len(progresses) > 0:
        # on each turn, update progress by speed mentioned in speeds
        update_progress(progresses, speeds)
        # dequeue all progress over or equal 100 and increment count
        while True:
            value = dequeue(progresses, speeds)
            if value is not None:
                count += 1
            else:
                break

        if count > 0:
            answer.append(count)
            count = 0

    return answer

def update_progress(progresses, speeds):
    i = 0
    while i < len(progresses):
        progresses[i] += speeds[i]
        i += 1

def dequeue(progresses, speeds):
    if  len(progresses) == 0:
        return None

    if progresses[0] < 100:
        return None

    speeds.pop(0)
    return progresses.pop(0)

if __name__ == "__main__":
    print(solution([93, 30, 55], [0, 30, 5]))
    print(solution([93, 30, 55], [1, 30, 5]))
    print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
    print(solution([], []))
    print(solution([1], [1]))
    print(solution([1,1,1,1,0], [1,1,1,1,1]))
# goal: 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
# stages가 매개변수로 주어질 때, 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는
# 배열을 return 하도록 solution 함수를 완성하라.

#   - 실패율은 다음과 같이 정의한다.
#       - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

#   - 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
#   - stages의 길이는 1 이상 200,000 이하이다.
#   - stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
#       - 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
#       - 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
#   - 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
#   - 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
def solution(N, stages):
    temp = []
    players = len(stages)

    i = 1
    # for each stage,
    while i < (N+1):
        if players == 0:
            temp.append([i, 0])
            i += 1
            continue

        # get number of people not passed the stage
        number_of_people_not_passed = count_not_passed(i, stages)

        # calculate failure rate
        failure_rate = number_of_people_not_passed / players
        # store [stage_number, failure rate] to temp
        temp.append([i, failure_rate])

        # update number of players
        players = players - number_of_people_not_passed
        i += 1

    # sort temp by failure rate
    temp = sorted(temp, key= lambda e: e[1], reverse=True)

    # place stage number to answer in order
    answer = [x[0] for x in temp]

    # return answer
    return answer


def count_not_passed(stage_number, stages):
    count = 0

    for stage in stages:
        if stage == stage_number:
            count +=1

    return count

if __name__ == "__main__":
    print(solution(4, [1,1,1,1,1])) #[1, 2, 3, 4]
    print(solution(4, [2,2,2,2,2])) #[1, 2, 3, 4]
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3])) #[3,4,2,1,5]
    print(solution(5, [4,4,4,4,4])) #[4,1,2,3,5]
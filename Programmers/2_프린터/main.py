# goal: 현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 내가 인쇄를 요청한 문서가
# 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 내가 인쇄를 요청한 문서가
# 몇 번째로 인쇄되는지 return 하도록 solution 함수를 작성해주세요.

# 제한사항
#   - 현재 대기목록에는 1개 이상 100개 이하의 문서가 있습니다.
#   - 인쇄 작업의 중요도는 1~9로 표현하며 숫자가 클수록 중요하다는 뜻입니다.
#   - location은 0 이상 (현재 대기목록에 있는 작업 수 - 1) 이하의 값을 가지며 대기목록의 가장 앞에 있으면 0, 두 번째에 있으면 1로 표현합니다.

from collections import deque

def solution(priorities, location):
    answer = 0
    queue_index = 1

    # map priorities to the form [(index, priority number), []]
    priorities = deque(enumerate(priorities))

    # while true
    while True:
    #   pop first element from list
        priority = priorities.popleft()
        #   if there is element in list with higher priority, then put back in.
        if higher_priority_exists(priority, priorities):
            priorities.append(priority)
            #   increment count
        else:
            #   otherwise,
            #   check if location match. if so, return count
            if priority[0] == location:
                return queue_index
            queue_index += 1
        #   increment count

    answer = queue_index
    return answer

def higher_priority_exists(priority, priorities):
    if len(priorities) == 0:
        return False

    has_higher_priority = priority[1] < max(priorities, key = lambda e: e[1])[1]
    if has_higher_priority:
        return True
    return False

if __name__ == "__main__":
    print(solution([1], 0)) #1
    print(solution([2,1], 1)) #2
    print(solution([2, 1, 3, 2], 2)) #1
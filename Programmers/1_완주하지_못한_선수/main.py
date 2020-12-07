def solution(participant, completion):
    answer = ''
    count = {}

    for person in participant:
        if person not in count:
            count[person] = 1
        else:
            count[person] += 1

    for person in completion:
        count[person] -= 1

    for person in count:
        if count[person] != 0:
            answer = person

    return answer
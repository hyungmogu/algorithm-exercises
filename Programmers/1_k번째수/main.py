def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0] - 1
        j = command[1] - 1
        k = command[2] - 1
        temp = array[i:j+1]
        temp.sort()
        answer.append(temp[k])
    return answer
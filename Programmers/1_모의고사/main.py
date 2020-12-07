def solution(answers):
    answer = []
    N = len(answers)
    person_1_answers = [1, 2, 3, 4, 5]
    person_2_answers = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3_answers = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    i = 0
    correct_count = [[1,0],[2,0],[3,0]]
    while i < N:
        # get answer for ith question
        correct_answer = answers[i]

        # get person 1's answer for ith question
        person_1_ans = person_1_answers[i % 5]
        # if is correct, add to count
        if correct_answer == person_1_ans:
            correct_count[0][1] += 1

        # get person 2's answer for ith question
        person_2_ans = person_2_answers[i % 8]
        # if is correct, add to count
        if correct_answer == person_2_ans:
            correct_count[1][1] += 1

        # get person 3's answer for ith question
        person_3_ans = person_3_answers[i % 10]
        # if is correct, add to count
        if correct_answer == person_3_ans:
            correct_count[2][1] += 1

        i += 1

    correct_count = sorted(correct_count, key=lambda e: e[1])
    highest = correct_count[2][1]

    for (person, count) in correct_count:
        if count == 0:
            continue

        if count == highest:
            answer.append(person)

    return answer
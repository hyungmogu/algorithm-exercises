def solution(prices):
    answer = []
    N = len(prices)
    i = 0
    while i < N:
        j = i+1
        count = 0

        # count number of items higher than current value
        if i != (N-1):
            while j < N:
                count += 1
                if prices[i] > prices[j]:
                    break
                j+=1

        # store count in array answer
        answer.append(count)

        i+=1

    return answer
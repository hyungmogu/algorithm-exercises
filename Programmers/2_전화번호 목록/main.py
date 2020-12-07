# goal: 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록
# solution 함수를 작성해주세요.
#   - phone_book의 길이는 1 이상 1,000,000 이하입니다.
#   - 각 전화번호의 길이는 1 이상 20 이하입니다.

def solution(phone_book):
    N = len(phone_book)
    i = 0
    while i < N:
        j = i +1
        while j < N:
            smaller_number = min(phone_book[i], phone_book[j])
            larger_number = max(phone_book[i], phone_book[j])
            if smaller_number in larger_number:
                return False

            j += 1
        i += 1

    answer = True
    return answer

if __name__ == "__main__":
    print(solution(["111", "2222", "333", "44444"]))
    print(solution(["111"]))
    print(solution(["111", "222"]))
    print(solution(["111", "111222"]))
    print(solution(["111222", "111"]))
# goal:  두 수 a ,b를 입력받아 2016년 a월 b일이 무슨 요일인지 리턴하는 함수, solution을
# 완성하세요
#   - 요일의 이름은 일요일부터 토요일까지 각각 SUN,MON,TUE,WED,THU,FRI,SAT 입니다

# 제한 조건
#   - 2016년은 윤년입니다.
#   - 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):
    number_of_days = 0
    day_label_by_distance_from_friday = {0: "FRI", 1: "SAT", 2: "SUN", 3: "MON", 4: "TUE",
                                         5: "WED", 6: "THU"}
    number_of_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    index = a -1
    number_of_days += sum(number_of_days_in_month[:index])

    number_of_days += b

    distance_from_friday = (number_of_days-1) % 7

    answer = day_label_by_distance_from_friday[distance_from_friday]

    return answer

if __name__ == "__main__":
    print(solution(1, 1)) #FRI
    print(solution(1, 2)) #SAT
    print(solution(1, 3)) #SUN
    print(solution(1, 4)) #MON
    print(solution(1, 5)) #TUE
    print(solution(1, 6)) #WED
    print(solution(1, 7)) #THU
    print(solution(1, 8)) #FRI
    print(solution(5, 24)) #TUES
    print(solution(10, 4))
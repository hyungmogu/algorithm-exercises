# goal: 문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때, 각 문자열의 인덱스 n번째 글자를
# 기준으로 오름차순 정렬하십시오.

# 제한사항
#   - strings는 길이 1 이상, 50이하인 배열입니다.
#   - strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
#   - strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
#   - 모든 strings의 원소의 길이는 n보다 큽니다.
#   - 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

def solution(strings, n):
    strings = sorted(strings)
    strings = sorted(strings, key = lambda e: e[n])
    return strings

if __name__ == "__main__":
    print(solution(["sun"], 1)) #sun
    print(solution(["sun", "bed", "car"], 1)) #[car, bed, sun]
    print(solution(["abce", "abcd", "cdx"], 2)) #[abcd, abce, cdx]
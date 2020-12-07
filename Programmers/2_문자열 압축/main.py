# goal: 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개 이상 단위로 문자열을 잘라
# 압축하여 표현한 문자열 중 가장 짧은 것의 길이를 return 하도록 solution 함수를 완성해주세요.

# 제한사항
#   - s의 길이는 1 이상 1,000 이하입니다.
#   - s는 알파벳 소문자로만 이루어져 있습니다.

import sys
def solution(s):
    N = len(s)
    minimum_length = sys.maxsize

    if len(s) == 1:
        return 1

    # while i < N where i represents length of compression string
    substring_length = 1
    while substring_length < N:
        # find the length of string after compression
        length_after_compression = compress_string(s,substring_length,N)
        # if length of string is less current, update minimum value
        minimum_length = min(minimum_length, length_after_compression)
        substring_length += 1

    # return minimum value
    answer = minimum_length
    return answer

def compress_string(s,substring_length,N):
    current_length = 0
    substrings_list = []
    substring_count = 0
    substring = ''
    prev_substring = ''
    compressed_string = ''
    i = 0

    while i < N:
        substring += s[i]
        current_length += 1
        if (current_length % substring_length == 0):
            substring_count += 1
            if prev_substring == substring:
                substrings_list[-1] = str(substring_count) + (substring) if substring_count > 1 else substring
            else:
                substrings_list.append(substring)
                substring_count = 1 if i != 0 else substring_count

            prev_substring = substring
            substring = ''

        i += 1

    if not all_substrings_added(substring):
        substrings_list.append(substring)

    return len(''.join(substrings_list))

def all_substrings_added(substring):
    return True if len(substring) == 0 else False

if __name__ == "__main__":
    print(solution("aabbaccc")) #7
    print(solution("ababcdcdababcdcd")) #9
    print(solution("abcabcdede")) #8
    print(solution("abcabcabcabcdededededede")) #14
    print(solution("xababcdcdababcdcd")) #17

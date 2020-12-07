# goal: 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는
# solution를 완성해주세요.

# 제한사항
# n은 10,000 이하의 자연수 입니다.

# Example
#   - 15
#       1 + 2 + 3 + 4 + 5 = 15 (yes) 1
#       2 + 3 + 4 + 5 + 6 = 20 (no)
#       3 + 4 + 5 + 6 = 18 (no)
#       4 + 5 + 6 = 15 (yes) 2
#       5 + 6 + 7 = 19 (no)
#       6 + 7 + 8 = 21 (no)
#       7 + 8 = 15 (yes) 3
# ...
#       15 = 15 (yes) 4

# There's 4 in total

# Pseudocode
#   for each number num ranging from 1 to n
#   add consecutive numbers of x to current_sum
#   if current_sum == n,
#       add to count
#       reset current_sum
#       break
#   if current_sum > n,
#       reset current_sum
#       break

def solution(n):
    count = 0
    current_sum = 0

    for num in range(1, n+1):
        current_sum += num

        while current_sum < n:
            num += 1
            current_sum += num

        if current_sum == n:
            count += 1

        current_sum = 0
    return count

if __name__ == "__main__":
    print(solution(15)) #4
    print(solution(1)) #1
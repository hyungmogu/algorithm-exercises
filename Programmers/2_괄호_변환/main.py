# goal: 균형잡힌 괄호 문자열 p가 매개변수로 주어질 때, 주어진 알고리즘을 수행해 올바른 괄호 문자열로
# 변환한 결과를 return 하도록 solution 함수를 완성해 주세요.
#   - 다음과 같은 과정을 통해 올바른 괄호 문자열로 변환할 수 있습니다.

#       -1. x 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
#       -2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.
#       -3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
#       -  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
#       -4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다.
#       -  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
#       -  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
#       -  4-3. ')'를 다시 붙입니다.
#       -  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
#       -  4-5. 생성된 문자열을 반환합니다.


def solution(p):
    answer = ''
    # if p is empty, return empty
    if p == "":
        return p

    answer = _solution(p)
    return answer

def _solution(w):
    result = ""
    if w == "":
        return ""

    # w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다
    u,v = get_u_and_v(w)

    # get closest 균형잡힌 괄호 문자열
    # if 문자열 u가 "올바른 괄호 문자열"
    if correctly_parenthesized(u):
        # 문자열 v에 대해 1단계부터 다시 수행합니다
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        return u + _solution(v)

    # if not u가 "올바른 괄호 문자열"
    # 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
    result += '('
    # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
    result += _solution(v)
    # ')'를 다시 붙입니다.
    result += ')'
    # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
    result += reverse(u[1:-1])

    # 생성된 문자열을 반환합니다.
    return result

def get_u_and_v(w):
    u = ''
    v = ''
    right_parenthesis = 0
    left_parenthesis = 0
    # get_u_and_v
    #   u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다.

    i = 0
    while i < len(w):
        if w[i] == "(":
            left_parenthesis += 1
        else:
            right_parenthesis += 1

        # at the moment left_parenthesis == right_parenthesis, slice string to index and store in u
        # store remainder in v
        if left_parenthesis == right_parenthesis:
            u = w[:i+1]
            break

        i += 1

    v = w[i+1:]
    # return u and v
    return u, v

def correctly_parenthesized(w):
    stack = Stack()

    for parenthesis in w:
        if parenthesis == "(":
            stack.push(parenthesis)
        else:
            left_parenthesis = stack.pop()
            if left_parenthesis == None:
                return False

    return True

def reverse(u):
    res = ''
    for parenthesis in u:
        if parenthesis == "(":
            res += ")"
        else:
            res += "("

    return res

class Stack:
    def __init__(self):
        self.stack_list = []

    def push(self, parenthesis):
        self.stack_list.append(parenthesis)

    def pop(self):

        if len(self.stack_list) == 0:
            return None

        return self.stack_list.pop()

if __name__ == "__main__":
    print(solution(")(")) #()
    print(solution("(()())()")) #(()())()
    print(solution("()))((()")) #()(())()
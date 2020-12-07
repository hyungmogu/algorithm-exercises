#goal: 게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가
# 담긴 배열 moves가 매개변수로 주어질 때, 크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를
# return 하도록 solution 함수를 완성해주세요.
#
#   - 만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다
#   - 크레인 작동 시 인형이 집어지지 않는 경우는 없다
#   - 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다
#
# 제한사항
#   - board 배열은 2차원 배열로 크기는 5 x 5 이상 30 x 30 이하입니다.
#   - board의 각 칸에는 0 이상 100 이하인 정수가 담겨있습니다.
#       - 0은 빈 칸을 나타냅니다.
#       - 1 ~ 100의 각 숫자는 각기 다른 인형의 모양을 의미하며 같은 숫자는 같은 모양의 인형을 나타냅니다.
#   - moves 배열의 크기는 1 이상 1,000 이하입니다.
#   - moves 배열 각 원소들의 값은 1 이상이며 board 배열의 가로 크기 이하인 자연수입니다.

from collections import deque

def solution(board, moves):
    basket = []
    N = len(board)
    board_by_columns = {}
    count = 0

    # extract columns and put each as queue in dictionary with column number as key
    i = 0
    while i < N:
        column = get_column(i, board)
        board_by_columns[(i+1)] = deque(column)
        i += 1

    # for each move,
    for move in moves:
        # get dolls in target column
        # take out the uppermost element from the column
        try:
            doll_board = board_by_columns[move].popleft()
        except IndexError:
            doll_board = None

        # check if last element in basket is the same as the taken out element
        #   if match, then add count, and pop the last element from the basket
        try:
            doll_basket = basket[-1]
        except IndexError:
            doll_basket = None

        if doll_board == None:
            continue

        if doll_board != doll_basket:
            basket.append(doll_board)
        else:
            count += 2
            basket.pop()
    answer = count
    return answer

def get_column(index, board):
    column = []
    for row in board:
        if row[index] == 0:
            continue
        column.append(row[index])

    return column

if __name__ == "__main__":
    solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
    # assert(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]) == 4)
# goal: 네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.
#   - 지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 공백(" ) 또는벽(#") 두 종류로 이루어져 있다.
#   - 전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 지도 1과 지도 2라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
#   - 지도 1과 지도 2는 각각 정수 배열로 암호화되어 있다.
#   - 암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
#   - 원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.
#

def solution(n, arr1, arr2):
    answer = []

    i = 0
    while i < n:
        # perform bitwise or on arr1[i] and arr2[i], store in combined_value
        combined_value = arr1[i] | arr2[i]

        # covert combined value to hash and spaces
        map_piece = convert_decimal_to_hash_and_spaces(combined_value, n)

        # store inside the array answer
        answer.append(map_piece)

        i += 1

    # return result
    return answer

def convert_decimal_to_hash_and_spaces(decimal_number,n):
    result = ""

    i = 0
    while i < n:
        if ((decimal_number >> i) & 1) == 0:
            result = " " + result
        else:
            result = "#" + result
        i += 1
    return result

if __name__ == "__main__":
    print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])) # ["#####","# # #", "### #", "# ##", "#####"]
    print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10])) #["######", "### #", "## ##", " #### ", " #####", "### # "]
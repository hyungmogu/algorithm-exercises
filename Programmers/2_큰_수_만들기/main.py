#goal: number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
# 하도록 solution 함수를 완성하세요.

# 제한 조건
#   - number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
#   - k는 1 이상 number의 자릿수 미만인 자연수입니다.

# cases


# k = 4 number="4177252841" stack=[]
#
# k = 4 number="4177252841" stack=[4]  stack empty --> add
#               ^
# k = 4 number="4177252841" stack=[4,1] 4 < 1 (false) --> continue
#                ^
# k = 2 number="4177252841" stack=[4]  1 < 7 (true) --> pop
#                 ^
# k = 1 number="4177252841" stack=[] 4 < 7 (true) --> pop
#                 ^
# k = 3 number="4177252841" stack=[7]
#                 ^
# k = 3 number="4177252841" stack=[7,7]
#                  ^
# k = 3 number="4177252841" stack=[7,7]
#                  ^

def solution(number, k):
    stack = []

    for i,num in enumerate(number):
        while stack and stack[-1] < num and  k > 0:
            stack.pop()
            k -= 1

        if k == 0:
            stack += number[i:]
            break

        stack.append(num)

    if k != 0:
        stack = stack[:-k]

    # return result
    answer = "".join(stack)
    return answer

# from collections import deque

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.prev = None
#         self.next = None

# class LinkedList:
#     def __init__(self, item_list):
#         self.head = Node(item_list[0])
#         self.end = None
#         N = len(item_list)
#         i = 1
#         while i < N:
#             self.append(Node(item_list[i]))
#             i += 1

#     def __str__(self):
#         answer = ""
#         current_node = self.head
#         while current_node != None:
#             answer += current_node.value
#             current_node = current_node.next

#         return answer

#     def append(self, node):
#         self.end = node
#         current_node = self.head

#         while current_node.next != None:
#             current_node = current_node.next

#         current_node.next = node
#         node.prev = current_node

#     def remove(self, node):
#         prev_node = node.prev
#         next_node = node.next

#         if prev_node == None:
#             self.head = next_node
#             next_node.prev = None

#         if next_node == None:
#             self.end = prev_node
#             prev_node.next = None

#         if prev_node != None and next_node != None:
#             next_node.prev = prev_node
#             prev_node.next = next_node


# def solution(number, k):
#     answer = ''

#     # convert number to queue
#     numbers_ll = LinkedList(number)
#     current_node = numbers_ll.head.next
#     # find biggest number after removing k
#     while k > 0 and current_node != None:
#         prev_node = current_node.prev
#         # start off with the second number i in list
#         # if number_list[i - 1] < number_list[i], then remove number
#         if prev_node.value < current_node.value:
#             numbers_ll.remove(prev_node)
#             # also decrement k
#             current_node = numbers_ll.head.next
#             k -= 1
#         else:
#             # else, move i by 1
#             current_node = current_node.next


#     while k > 0:
#         numbers_ll.remove(numbers_ll.end)
#         k -= 1

#     # return result
#     answer = str(numbers_ll)
#     return answer

if __name__ == "__main__":
    print(solution("1924", 2)) #94
    print(solution("1231234", 3)) #3234
    print(solution("1111", 2)) #11
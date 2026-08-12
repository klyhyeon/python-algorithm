# n개의 음이 아닌 정수들이 있습니다. 이 정수들을 순서를 바꾸지 않고 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
#
# 제한사항
# 주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
# 각 숫자는 1 이상 50 이하인 자연수입니다.
# 타겟 넘버는 1 이상 1000 이하인 자연수입니다.
# 입출력 예
# numbers	target	return
# [1, 1, 1, 1, 1]	3	5
# [4, 1, 2, 1]	4	2
# 입출력 예 설명
# 입출력 예 #1
#
# 문제 예시와 같습니다.
#
# 입출력 예 #2
#
# +4+1-2+1 = 4
# +4-1+2-1 = 4이
# 총 2가지 방법이 있으므로, 2를 return 합니다.

# 2차 시도 성공
def solution(numbers, target):
    return dfs(numbers, target, 0, numbers[0]) + dfs(numbers, target, 0, -numbers[0])


# target을 만들 수 있는 개수 반환
def dfs(numbers, target, idx, total) -> int:
    if idx == len(numbers) - 1:
        if target == total:
            return 1
        else:
            return 0
    return dfs(numbers,target, idx + 1, total + numbers[idx + 1]) + dfs(numbers,target, idx + 1, total - numbers[idx + 1])


print(solution([1,1,1,1,1], 3))

# 실패 풀이 30분 소요
# def solution(numbers, target):
#     sum_total = 0
#     sum_total2 = 0
#     return dfs(0, numbers, True, sum_total) + dfs(0, numbers, False, sum_total2)
#
#
# def dfs(idx, numbers, is_sum, sum_total) -> int:
#     size = len(numbers) - 1
#     if idx == size:
#         if is_sum:
#             return numbers[idx]
#         else:
#             return -numbers[idx]
#     else:
#         sum_total += dfs(idx + 1, numbers, True)
#         sum_total += dfs(idx + 1, numbers, False)

# 정답 풀이
# def solution(numbers, target):
#     def dfs(idx, total):
#         if idx == len(numbers):
#             return 1 if total == target else 0
#         return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

#     return dfs(0, 0)

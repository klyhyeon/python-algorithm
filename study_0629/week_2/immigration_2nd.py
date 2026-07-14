# https://school.programmers.co.kr/learn/courses/30/lessons/43238
# n	times	return
# 6	[7, 10]	28
# 제한사항
# 입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
# 각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
# 심사관은 1명 이상 100,000명 이하입니다.
# n: 사람 수
# times: 심사관마다 걸리는 시간
# 최악의 소요시간과 1 사이의 이분탐색. 심사관들마다 target 시간 내에 진행할 수 있는 사람들 합이 n과 일치하거나 큰 최소 시간이 정답

def solution(n, times: list):
    final_answer = 0
    left = 1
    right = max(times) * n
    while (left <= right):
        middle = (left + right) // 2
        customers = get_customers_count(middle, times)
        # customer를 만족시켜도 더 적은 시간으로 충족시킬수도 있음
        if customers >= n:
            final_answer = middle
            right = middle - 1
        elif customers < n:
            left = middle + 1
    return final_answer

# time_limit 마다 최대로 쳐낼 수 있는 입국자 수
def get_customers_count(time_limit, times):
    answer = 0
    for time in times:
        answer += time_limit // time
    return answer

print(solution(5, [6, 12, 15, 20]))
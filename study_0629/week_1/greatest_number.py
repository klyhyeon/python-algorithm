# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 정렬
# 가장 큰 수
# 문제 설명
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

# 예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

# 제한 사항
# numbers의 길이는 1 이상 100,000 이하입니다.
# numbers의 원소는 0 이상 1,000 이하입니다.
# 정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
# 입출력 예
# numbers	return
# [6, 10, 2]	"6210"
# [3, 30, 34, 5, 9]	"9534330"
# 배열 크기 100,000 이하
# 숫자 크기 1,000이하
# 소요시간: 30분 (제출 후 테스트 실패)
# 접근방식: 앞자리가 같은 경우 맨 끝자리만 비교해 큰 값과 
# 참고 접근방식: https://smcho1201.tistory.com/81


def solution(numbers):
    answer = '2'
    # 문자로 정렬하되, 30, 3인 경우 더 큰 값이 3이여야 함.
    # 1. 문자로 변환
    numbers_str = list(map(str, numbers))
    # 2. 내림차순 정렬
    numbers_str.sort(reverse = True)
    # 3. 30, 3인 경우 더 큰 값이 3이여야 함
    print(numbers_str)
    for i in range(len(numbers_str)):
        if (i != 0) and (numbers_str[i - 1][0] == numbers_str[i][0]):
            len_range = max(len(numbers_str[i - 1]), len(numbers_str[i]))
            for i in range(len_range):
                if numbers_str[i - 1][]
            if (int(numbers_str[i - 1][-1])) < (int(numbers_str[i][-1])):
                pre_number = numbers_str[i - 1]
                numbers_str[i - 1] = numbers_str[i]
                numbers_str[i] = pre_number
    return "".join(numbers_str)

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
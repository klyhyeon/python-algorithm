# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# Key Idea: Find two numbers in a sorted array that sum to a target.
# Consider: Can you leverage the sorted property to solve this in one pass?
# Current complexity: O(N^2)
# Suggested complexity: O(N)
# Suggestions: Use two pointers to achieve linear time complexity.
# AI가 제안한 시간 복잡도 향상 코드 (bisect algorithm)
# bisect algorithm function in Python (https://docs.python.org/3/library/bisect.html)
# - 배열에 값을 삽입해도 정렬이 유지된다
# - 길이가 큰 배열에서 값을 찾거나 비교할때 짧은 시간 내 탐색한다

#  정렬된 배열에서 범위 내 개수 세기
#   정렬된 정수 배열 nums와 여러 개의 쿼리 [lo, hi]가 주어진다.
#   각 쿼리에 대해 lo <= x <= hi인 nums의 원소 개수를 반환하라.
#   입력:
#     nums = [1, 3, 3, 5, 7, 7, 7, 9, 11]
#     queries = [[3, 7], [4, 4], [1, 11], [8, 10]]
#   출력: [6, 0, 9, 1]
#   제약:
#     1 <= len(nums) <= 100,000
#     1 <= len(queries) <= 100,000

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        answer = list()
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target: return [left + 1, right + 1]
            elif s < target: left += 1
            else: right -= 1
        return answer


sol = Solution()
print(sol.twoSum([0,0,3,4], 0))
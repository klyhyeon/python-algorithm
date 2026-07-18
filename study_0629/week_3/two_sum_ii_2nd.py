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
# AI가 제안한 시간 복잡도 향상 코드 (Two pointer)

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
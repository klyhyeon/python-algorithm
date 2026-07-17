# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.
# 소요시간: 15분
# Key Idea: Find two numbers in a sorted array that sum to a target.
# Consider: Can you leverage the sorted property to solve this in one pass?
# Current complexity: O(N^2)
# Suggested complexity: O(N)
# Suggestions: Use two pointers to achieve linear time complexity.

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 2 numbers sum to target. numbers asc order
        # for loop with numbers ele, value exists with (target - ele) in array
        # length = 30,000
        answer = list()
        for idx, number in enumerate(numbers):
            left_number = target - number
            try:
                left_number_idx = numbers.index(left_number, idx + 1, len(numbers))
                answer.append(idx + 1)
                answer.append(left_number_idx + 1)
                return answer
            except ValueError:
                continue
        return answer


sol = Solution()
print(sol.twoSum([0,0,3,4], 0))
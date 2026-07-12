# https://leetcode.com/problems/binary-search/description/
# nums: array asc ordered
# target: number
# target exists, return index
# You must write an algorithm with O(log n) runtime complexity.
# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1

# Constraints:

# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4
# All the integers in nums are unique.
# nums is sorted in ascending order.
# 소요시간: 50분
# last != middle 조건 때문에 첫 시도 실패, 이후 성공
# Current complexity: O(logN)
# Suggested complexity: O (logN)
# Suggestions: Excellent work. The complexity is optimal and no further changes are needed.

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        last = len(nums) - 1
        middle: int = last // 2
        while (True):
            if target > nums[middle] and last != middle:
                middle = (last + middle + 1) // 2
            elif target < nums[middle] and last != middle:
                last = middle - 1
                middle = last // 2
            elif target == nums[middle]:
                return middle
            elif last == middle:
                return -1
            
solution = Solution()
print(solution.search([1,2,3,4,5,6,7,8,9,10], 2))
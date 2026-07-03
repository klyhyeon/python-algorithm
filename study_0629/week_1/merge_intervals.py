# https://leetcode.com/problems/merge-intervals/description/
# 56. Merge Intervals


# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# Example 3:

# Input: intervals = [[4,7],[1,4]]
# Output: [[1,7]]
# Explanation: Intervals [1,4] and [4,7] are considered overlapping.


# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

# 겹치는 구간을 병합해서 구간들이 서로 겹치지 않도록 반환
# 소요시간: 42분 (실패)
# 테스트 

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 상대방과 겹치는 조건
        # 1. 내 start < 상대 end < 내 end
        # 2. 내 start < 상대 start < 내 end
        # 3. 내 start == 상대 start, 내 start == 상대 end
        # 4. 내 end == 상대 start, 내 end == 상대 end
        # 병햡되면 기존 아이템은 리스트에서 제거, 또는 신규 리스트에 추가
        # 1. 병합 범위는 min(내 start, 상대 start), max(내 end, 상대 end)
        answer = list()
        if len(intervals) == 1:
            return intervals
        
        for i in range(len(intervals) - 1):
            for j in range(len(intervals) - 1):
                current_inter = intervals[i]
                other_inter = intervals[j]
                current_inter_start = current_inter[0]
                current_inter_end = current_inter[1]
                other_inter_start = other_inter[0]
                other_inter_end = other_inter[1]
                if current_inter_start < other_inter_end < current_inter_end:
                    intervals.append(self._merge_items(current_inter, other_inter))
                    self._remove_current_other(i, j, intervals)
                elif current_inter_start < other_inter_start < current_inter_end:
                    intervals.append(self._merge_items(current_inter, other_inter))
                    self._remove_current_other(i, j, intervals)
                elif current_inter_start == other_inter_start or current_inter_start == other_inter_end:
                    intervals.append(self._merge_items(current_inter, other_inter))
                    self._remove_current_other(i, j, intervals)
                elif current_inter_end == other_inter_start or current_inter_end == other_inter_end:
                    intervals.append(self._merge_items(current_inter, other_inter))
                    self._remove_current_other(i, j, intervals)
        return intervals

    
    def _merge_items(self, current_inter, other_inter) -> List:
        return [min(current_inter[0], other_inter[0]), max(current_inter[1], other_inter[1])]
    
    def _remove_current_other(self, i, j, intervals):
        if i > j:
            del intervals[i]
            del intervals[j]
        else:
            del intervals[j]
            del intervals[i]

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))


# self, 클래스 내 메서드 관련 내용 공부


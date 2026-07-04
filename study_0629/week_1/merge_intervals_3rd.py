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
# 첫 번째 시도와 달리 기존 리스트에서 제거하지 않고 신규 리스트를 추가하거나 다른 방법 사용
# 소요시간: 
# 예외: [1,4],[0,2],[3,5]

from typing import List


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer: List = list()
        # 정렬하면 바로 뒷 숫자 배열과 answer의 맨 나중의 배열만 비교하면 된다
        intervals.sort(key = lambda x : x[0])
        for index, item in enumerate(intervals):
            if answer and answer[-1][1] >= item[1]:
                continue
            if index == len(intervals) - 1:
                if answer and answer[-1][1] >= item[1]:
                    answer.append(intervals[index + 1])
                    break
                else:
                    answer.append(item)
                    break
            if item[1] >= intervals[index + 1][0]:
                if answer and answer[-1][1] >= intervals[index + 1][0]:
                    new_answer = [answer[-1][0], max(answer[-1][1], intervals[index + 1][1])]
                    answer.pop()
                    answer.append(new_answer)
                else:
                    answer.append([item[0], max(item[1], intervals[index + 1][1])])
            else:
                answer.append(item)
        return answer

sol = Solution()
print(sol.merge([[1,4],[0,2],[3,5]]))


# self, 클래스 내 메서드 관련 내용 공부


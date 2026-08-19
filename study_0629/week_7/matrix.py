#542. 01 Matrix
# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
#
# The distance between two cells sharing a common edge is 1.
#
# Example 1:
#
# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:
#
# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
#
# Constraints:
#
# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.
# 실패: 소요시간 30분

# 정답코드
from collections import deque

class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        queue = deque()

        # 1. 값이 0인 모든 좌표를 큐에 넣고, 1인 값은 -1로 초기화
        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    queue.append((r, c))
                else:
                    mat[r][c] = -1

        # 4방향 이동 (상, 하, 좌, 우)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # 2. Multi-Source BFS
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 격자 범위 내에 있고, 아직 방문하지 않은 칸(-1)인 경우
                if 0 <= nr < m and 0 <= nc < n and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1
                    queue.append((nr, nc))

        return mat

# from typing import List

# class Solution:
#     def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
#         x_move = [1, -1, 0, 0]
#         y_move = [0, 0, 1, -1]
#         row_len = len(mat)
#         col_len = len(mat[0])
#         for i in range(row_len):
#             for j in range(col_len):
#                 print(mat[i][j])
#         return []

Solution().updateMatrix([[0,0,0],[0,1,0],[0,0,0]])


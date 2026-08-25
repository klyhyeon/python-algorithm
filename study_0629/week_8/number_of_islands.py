#Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        i_move = [0, 0, 1, -1]
        j_move = [1, -1, 0, 0]
        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == '1':
                    self.dfs(i, j, i_move, j_move, cols, rows, visited, grid)
                    answer += 1
        return answer

    def dfs(self, i, j, i_move, j_move, cols, rows, visited, grid):
        visited[i][j] = True
        for n in range(4):
            new_i = i + i_move[n]
            new_j = j + j_move[n]
            if 0 <= new_i < rows and 0 <= new_j < cols:
                if not visited[new_i][new_j] and grid[new_i][new_j] == '1':
                    self.dfs(new_i, new_j, i_move, j_move, cols, rows, visited, grid)

print(Solution().numIslands( [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))


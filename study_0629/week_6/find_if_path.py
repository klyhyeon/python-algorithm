# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

# You want to determine if there is a valid path that exists from vertex source to vertex destination.

# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.



# Example 1:


# Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
# Output: true
# Explanation: There are two paths from vertex 0 to vertex 2:
# - 0 → 1 → 2
# - 0 → 2
# Example 2:


# Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
# Output: false
# Explanation: There is no path from vertex 0 to vertex 5.


# Constraints:

# 1 <= n <= 2 * 105
# 0 <= edges.length <= 2 * 105
# edges[i].length == 2
# 0 <= ui, vi <= n - 1
# ui != vi
# 0 <= source, destination <= n - 1
# There are no duplicate edges.
# There are no self edges.
# 실패: 40분 소요


from typing import List
from collections import defaultdict


# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
#         print(not [])
#         edges_dict = defaultdict(list)
#         for edge in edges:
#             edges_dict[edge[0]].append(edge[1])
#         return self.dfs(source, edges_dict, edges_dict[source], destination)

#     def dfs(self, source: int, edges_dict, connections: List[int], dest: int) -> bool:
#         if not connections:
#             return False
#         if dest in connections:
#             return True
#         for connection in connections:
#             if self.dfs(connection, edges_dict, edges_dict[connection], dest):
#                 return True

#
#
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # 1. Build bidirectional adjacency list
        edges_dict = defaultdict(list)
        for u, v in edges:
            edges_dict[u].append(v)
            edges_dict[v].append(u)

        visited = set()

        return self.dfs(source, edges_dict, destination, visited)

    def dfs(self, current: int, edges_dict: dict, dest: int, visited: set) -> bool:
        # Base case 1: Reached destination
        if current == dest:
            return True

        visited.add(current)

        # Traverse neighbors
        for neighbor in edges_dict[current]:
            if neighbor not in visited:
                # Catch the True returned from deeper calls!
                if self.dfs(neighbor, edges_dict, dest, visited):
                    return True

        return False

print(Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))

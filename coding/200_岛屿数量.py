"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。
岛屿总是被水包围，并且每座岛屿只能由水平方向或竖直方向上相邻的陆地连接形成。
此外，你可以假设该网格的四条边均被水包围。

示例 1:
输入:
11110
11010
11000
00000
输出: 1

示例 2:
输入:
11000
11000
00100
00011
输出: 3
解释: 每座岛屿只能由水平和/或竖直方向上相邻的陆地连接而成。

解题思路：
依次遍历 grid 中的每一个点，当出现“1”时，对该点进行 DFS 搜索，并将沿途搜索到“1”的点置为“0”；这个过程可以形象的理解成是“感染”！
对1个点DFS后，该点所能到达的所有为“1”的点都已经被感染成了“0”，此时岛屿总数量+1
易错点：
注意递归边界的判断！
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid: return 0
        m, n = len(grid), len(grid[0])
        
        def infect(grid, m, n, i, j): # 感染函数
            # 递归边界！
            # 注意 grid[i][j] == '0' 的判断一定要放在最后进行，以免数据索引越界！
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == '0':
                return
            grid[i][j] = "0" # 1 --> 0
            # 4个方向依次搜索
            infect(grid, m, n, i+1, j)
            infect(grid, m, n, i-1, j)
            infect(grid, m, n, i, j+1)
            infect(grid, m, n, i, j-1)
        
        cot = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1': # 可以被感染
                    infect(grid, m, n, i, j)
                    cot += 1
        return cot

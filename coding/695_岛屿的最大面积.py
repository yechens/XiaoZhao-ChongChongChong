"""
给定一个包含了一些 0 和 1 的非空二维数组 grid 。
一个 岛屿 是由一些相邻的 1 (代表土地) 构成的组合，这里的「相邻」要求两个 1 必须在水平或者竖直方向上相邻。你可以假设 grid 的四个边缘都被 0（代表水）包围着。
找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 0 。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是 11 ，因为岛屿只能包含水平或垂直的四个方向的 1 。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

解题思路：
经典的DFS题，与 200.岛屿数量 类似，可以用一个“感染函数”去感染某一个点1出发，所能到达的所有值为1的点（按上下左右4个方向递归搜索）
易错点：
1）注意递归边界
2）已经感染的点，值需要改变以免造成重复搜索
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid: return 0

        m, n = len(grid), len(grid[0])
        self.mmax = 0
        self.cot = 0 # 保存每次感染时所能获得的最大面积! 要为全局变量！

        def infect(grid, m, n, i, j, cot=0): # 感染函数
            if (not 0<=i<m) or (not 0<=j<n) or grid[i][j] != 1:
                return
            self.cot += 1
            if self.cot > self.mmax: self.mmax = self.cot
            directions = [[0,1],[0,-1],[1,0],[-1,0]] # 往4个方向去感染
            grid[i][j] = 2 # 标记岛屿中该位置已经被感染，避免重复搜索
            for d in directions:
                newi = i + d[0]
                newj = j + d[1]
                infect(grid, m, n, newi, newj, cot)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.cot = 0 # cot 刚开始都为0
                    infect(grid, m, n, i, j, self.cot)
        
        return self.mmax

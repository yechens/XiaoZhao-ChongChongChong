"""
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。

示例:
输入: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4

解题思路：
构建二维的 dp 数组，其中 dp[i][j] 表示以第i行第j列为右下角所能构成的最大正方形边长
状态转移方程：dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
可以理解为当前格子的最大变长取决于 “左边、上边、左上” 三个位置变长的最小值 + 1
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        # 初始化 第一行和第一列
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])

        for i in range(1, m):
            for j in range(1, n):
                # 只考虑包含1的格子，否则不可能构成有效的正方形
                if matrix[i][j] == '1':
                    dp[i][j] =  min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        print(dp)
        edge = max(dp[i][j] for i in range(m) for j in range(n))
        return edge * edge

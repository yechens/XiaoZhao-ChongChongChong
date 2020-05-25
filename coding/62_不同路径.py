'''
题目描述：
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

例如，上图是一个7 x 3 的网格。有多少可能的路径？

 

示例 1:

输入: m = 3, n = 2
输出: 3
解释:
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向右 -> 向下
2. 向右 -> 向下 -> 向右
3. 向下 -> 向右 -> 向右
示例 2:

输入: m = 7, n = 3
输出: 28
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 10 ^ 9

解题思路：
dp：二维数组
dp[i][j]表示到达j位置的路径条数
转移方程：
（首先行列位置满足在方格中这个条件）
dp[i][j]=dp[i-1][j]+dp[i][j-1]

'''


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #初始化
        dp=[[0]*(n)]*(m)
        #dp[i][j]表示到达j位置的路径条数
        dp[0][0]=1
        for irow in range(m):
            for icol in range(n):
                if irow==0 and icol==0:
                    continue
                else:
                    dp[irow][icol]=\
                    (dp[irow-1][icol] if irow-1>=0 and irow-1<m else 0)\
                    +(dp[irow][icol-1]  if icol-1>=0 and icol-1<n else 0)
                    
        return dp[-1][-1]
                

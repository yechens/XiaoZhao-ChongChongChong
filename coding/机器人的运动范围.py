'''
题目描述：
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？

 

示例 1：

输入：m = 2, n = 3, k = 1
输出：3
示例 2：

输入：m = 3, n = 1, k = 0
输出：1

解题思路：
DFS
注意：新的判断是否有效这个条件

'''


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        #DFS
        #0-未遍历
        #1-能遍历
        #2-不能走
        state=[[0 for _  in range(n)] for _ in range(m)]
        def iscorrect(i,j):
            cod1=(i>=0and i<m and j>=0 and j<n)
            return cod1 
        def sumcon(i,j):
            i=str(i)
            j=str(j)
            sumij=0
            for ic in i:
                sumij+=int(ic)
            for jc in j:
                sumij+=int(jc)
            return  sumij<=k
        def DFS(irow,icol):
            if not iscorrect(irow,icol) or state[irow][icol]!=0:
                return
            if not sumcon(irow,icol):
                state[irow][icol]=2
                return 
            else:
                state[irow][icol]=1
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                DFS(irow+i,icol+j)

        DFS(0,0)
        res=0
        for irow in range(m):
            for icol in range(n):
                if state[irow][icol]==1:
                    res+=1
        return res

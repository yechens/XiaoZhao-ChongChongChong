'''
题目描述:
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

解题思路：
DFS
注意state要恢复


'''

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #DFS
        
        def iscorrect(i,j):
            cod1=(i>=0and i<m and j>=0 and j<n)
            return cod1 
        def DFS(irow,icol,target,state):
            if target=='':
                return True
            if not iscorrect(irow,icol) or state[irow][icol]!=0:
                return False
            if board[irow][icol]!=target[0]:
                return False
            state[irow][icol]=1
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                if DFS(irow+i,icol+j,target[1:],state):
                    return True
            #恢复状态（不恢复上一步回不去了）
            state[irow][icol]=0
            return False
        state=[[0 for _  in range(len(board[0]))] for _ in range(len(board))]
        m=len(board)
        n=len(board[0])
        for irow in range(m):
            for icol in range(n):
                
                if DFS(irow,icol,word,state):
                    return True
        return False

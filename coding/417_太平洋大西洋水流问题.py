'''
题目描述：
给定一个 m x n 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

 

提示：

输出坐标的顺序不重要
m 和 n 都小于150
 

示例：

 

给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).

解题思路：
（辣鸡系统-执行代码的测试样例判断是有顺序的，但提交不是）
方法一：DFS遍历（超时，原因未知 ）
方法二：DFS逆流遍历，因为能逆流到的顺流就能够到达，不需要常规的状态数据存储状态！因为有
        res保存能逆流到的位置，同时还有高度限制，因此不会有重复遍历的点


'''




class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix :return None
        #DFS逆流
        def iscorrectpos(row,col):
            return True if row<len(matrix) and row>=0 and col <len(matrix[0]) and col>=0 else False
        #逆流的情况下能到达的点，顺流都可以到某一大洋
        def DFS(row,col,matrix,res):
            res.add((row,col))
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                if  iscorrectpos(row+i,col+j)  and matrix[row][col]<= matrix[row+i][col+j] and (row+i,col+j) not in res:
                    DFS(row+i,col+j,matrix,res)     
        #太平洋
        res1=set()
        #大西洋
        res2=set()
        #太平洋逆流
        for irow in range(len(matrix)):
            DFS(irow,0,matrix,res1)
        for icol in range(len(matrix[0])):
            DFS(0,icol,matrix,res1)
        #大西洋逆流
        for irow in range(len(matrix)):
            DFS(irow,len(matrix[0])-1,matrix,res2)
        for icol in range(len(matrix[0])):
            DFS(len(matrix)-1,icol,matrix,res2)

        return res1 & res2
        
        #DFS 顺流超时??????草！！！
        def iscorrectpos(row,col):
            return True if row<len(matrix) and row>=0 and col <len(matrix[0]) and col>=0 else False
        def DFS(row,col,matrix,reached_set,res_map):
            #判断边界
            if row==len(matrix)-1 or col==len(matrix[0])-1:
                reached_set.append('大西洋')
            if  row==0 or col==0:
                reached_set.append('太平洋')
            if len(set(reached_set))==2:
                 return reached_set
            #上下左右
            for i,j in [(1,0),(0,1),(-1,0),(0,-1)]:
                if  iscorrectpos(row+i,col+j)  and matrix[row][col]>= matrix[row+i][col+j]:
                    reached_set+=DFS(row+i,col+j,matrix,reached_set,res_map)
                    if len(set(reached_set))==2:
                        return reached_set
            return reached_set
        res=[]
        res_map=[[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
        for irow in range(len(matrix)):
            for icol in range(len(matrix[0])):
                #status=[[0 for _ in range(len(matrix[0]))]for _ in range(len(matrix))]
                reached_set=DFS(irow,icol,matrix,list(),res_map)
                 
                if len(set(reached_set))==2:
                    res.append([irow,icol])
        return res

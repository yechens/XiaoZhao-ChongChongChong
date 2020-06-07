class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
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

        return res1& res2
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

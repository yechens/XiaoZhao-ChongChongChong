'''
题目描述：
给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。

示例 1:

输入:
[
   [1,0,1],
   [0,0,1],
   [0,0,1]
]
输出: [1,0,2]
解释: 输入中 0 代表黑色，1 代表白色，标粗的元素即为满足条件的最大子方阵
示例 2:

输入:
[
   [0,1,1],
   [1,0,1],
   [1,1,0]
]
输出: [0,0,1]
提示：

matrix.length == matrix[0].length <= 200

解题思路：
1.从右下往左上dp_right_up
dp_right_up[i][j]=（lenght_right,length_down）表示当前位置往右,往下的最长0边
2.从左上往右下dp_left_down
dp_left_down[i][j]=（lenght_left,length_up）表示当前位置往左,往上的最长0边
3.从左上往右下 遍历


易错点：只要求矩形边，不要求内部
关键点：dp的含义
TODO：时间优化



'''

class Solution:
    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        def iscorrect(i,j):
            return 0<=i<len(matrix) and 0<=j<len(matrix)
        #dp[i][j]表示当前位置能够形成方阵的边长
        dp_right_up=[[[0,0] for _ in range(len(matrix))] for _ in range(len(matrix))]
        #右下到左上↖️ 
        for irow in range(len(matrix)-1,-1,-1):
            for icol in range(len(matrix)-1,-1,-1):
                if matrix[irow][icol]==1:
                    continue
                else:
                    dp_right_up[irow][icol]=[1,1]
                    #右边

                    if iscorrect(irow,icol+1):
                        dp_right_up[irow][icol][0]=dp_right_up[irow][icol][0]+dp_right_up[irow][icol+1][0]
                    if iscorrect(irow+1,icol):
                        dp_right_up[irow][icol][1]=dp_right_up[irow][icol][1]+dp_right_up[irow+1][icol][1]
        
        #左上到右下↘️

        dp_left_down=[[[0,0] for _ in range(len(matrix))] for _ in range(len(matrix))]
        for irow in range(len(matrix)):
            for icol in range(len(matrix)):
                if matrix[irow][icol]==1:
                    continue
                else:
                    dp_left_down[irow][icol]=[1,1]
                    #右边

                    if iscorrect(irow,icol-1):
                        dp_left_down[irow][icol][0]=dp_left_down[irow][icol][0]+dp_left_down[irow][icol-1][0]
                    if iscorrect(irow-1,icol):
                        dp_left_down[irow][icol][1]=dp_left_down[irow][icol][1]+dp_left_down[irow-1][icol][1]
        

        #融合
        max_res=-1
        max_res_pos=None
        for irow in range(len(matrix)):
            for icol in range(len(matrix)):
                if matrix[irow][icol]==1:
                    continue
                if irow==0 and icol==1:
                    print(dp_right_up[irow][icol])
                    
                row_length,col_length=dp_right_up[irow][icol]
                edge_lenght_one=min(row_length,col_length)
                add_lenght=1
                tmp_res=1
                tmp_pos=[irow,icol]
                for iadd in range(1,edge_lenght_one):#对角线
                    if irow==0 and icol==1:
                        print('iadd:',iadd)
                    if not iscorrect(irow+iadd,icol+iadd):continue
                    edge_length_two=min(dp_left_down[irow+iadd][icol+iadd])
                    #
                    height=iadd+1
                    if edge_length_two>=height-1 and edge_lenght_one>=height-1:
                        if edge_length_two>=height or edge_lenght_one>=height:
                            tmp_res=height
                    #else:
                    #    break
                #if irow==0 and icol==1:
                #        print('tmp_res:',tmp_res,max_res)
                if tmp_res>max_res:
                    max_res=tmp_res
                    max_res_pos=[irow,icol]
        if not max_res_pos:return []
        max_res_pos.append(max_res)
        return max_res_pos

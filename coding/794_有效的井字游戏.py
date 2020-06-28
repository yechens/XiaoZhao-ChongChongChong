'''
题目描述:
用字符串数组作为井字游戏的游戏板 board。当且仅当在井字游戏过程中，玩家有可能将字符放置成游戏板所显示的状态时，才返回 true。

该游戏板是一个 3 x 3 数组，由字符 " "，"X" 和 "O" 组成。字符 " " 代表一个空位。

以下是井字游戏的规则：

玩家轮流将字符放入空位（" "）中。
第一个玩家总是放字符 “X”，且第二个玩家总是放字符 “O”。
“X” 和 “O” 只允许放置在空位中，不允许对已放有字符的位置进行填充。
当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
当所有位置非空时，也算为游戏结束。
如果游戏结束，玩家不允许再放置字符。
示例 1:
输入: board = ["O  ", "   ", "   "]
输出: false
解释: 第一个玩家总是放置“X”。

示例 2:
输入: board = ["XOX", " X ", "   "]
输出: false
解释: 玩家应该是轮流放置的。

示例 3:
输入: board = ["XXX", "   ", "OOO"]
输出: false

示例 4:
输入: board = ["XOX", "O O", "XOX"]
输出: true
说明:

游戏板 board 是长度为 3 的字符串数组，其中每个字符串 board[i] 的长度为 3。
 board[i][j] 是集合 {" ", "X", "O"} 中的一个字符。


解题思路:
方法1:递归所有情况递归判断，尤其是判断结束条件
TODO：
方法2:情况分类讨论O(1)???




'''



from copy import deepcopy
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        #X 的数量不少与O
        x_count=0
        o_count=0
        for irow in range(3):
            for icol in range(3):
                if board[irow][icol]=='X':
                    x_count+=1
                if board[irow][icol]=='O':
                    o_count+=1
        if o_count>x_count:
            return False
        state=[[0 for _ in range(3)] for _ in range(3)]
        #行列计数
        self.row_x_count=[0,0,0]
        self.col_x_count=[0,0,0]
        self.row_o_count=[0,0,0]
        self.col_o_count=[0,0,0]
        #获取初始状态
        for irow in range(3):
            for icol in range(3):
                if board[irow][icol]=='O':
                    self.row_o_count[irow]+=1
                    self.col_o_count[icol]+=1
                if board[irow][icol]=='X':
                    self.row_x_count[irow]+=1
                    self.col_x_count[icol]+=1
        #判断是否为终止状态
        def is_finished(state,row_x_count,col_x_count,row_o_count,col_o_count):
            #所有位置非空
            if sum(row_x_count)+sum(col_x_count)+sum(row_o_count)+sum(col_o_count)==18:
                return True
            #3个相同字符的行，列，对角线
            if 3 in row_x_count or\
            3 in col_x_count or\
            3 in row_o_count or\
            3 in col_o_count:
                return True
            if state[0][0]=='X' and state[1][1]=='X' and state[2][2]=='X':
                return True 
            if state[0][2]=='X' and state[1][1]=='X' and state[2][0]=='X':
                return True 
            if state[0][0]=='O' and state[1][1]=='O' and state[2][2]=='O':
                return True     
            if state[0][2]=='O' and state[1][1]=='O' and state[2][0]=='O':
                return True 
            return False
        #递归
        start_state=int(is_finished(board,self.row_x_count,self.col_x_count,self.row_o_count,self.col_o_count))
        all_char_count=x_count+o_count

        def recursive(board,row_x_count,col_x_count,row_o_count,col_o_count,pop_char,finish_state_count,all_char_count,start_state):
            #终止条件所有位置为空,状态是否和起始位置一致
            if all_char_count==0:return int(finish_state_count)==start_state
            if finish_state_count>start_state:return False
            tmp_res=[]
            #判断是否有符合条件
            trigger=0
            for irow in range(3):
                for icol in range(3):
                    if pop_char=='O' and board[irow][icol]=='O':
                        trigger+=1
                        new_board=deepcopy(board)
                        #去掉O
                        new_board[irow]=new_board[irow][:icol]+' '+new_board[irow][icol+1:]
                        new_row_x_count=deepcopy(row_x_count)
                        new_col_x_count=deepcopy(col_x_count)
                        new_row_o_count=deepcopy(row_o_count)
                        new_col_o_count=deepcopy(col_o_count)
                        new_row_o_count[irow]-=1
                        new_col_o_count[icol]-=1
                        #判断是否为终止状态
                        
                        tmp_state=int(is_finished(new_board,new_row_x_count,new_col_x_count,new_row_o_count,new_col_o_count))
                        

                        res=recursive(new_board,new_row_x_count,new_col_x_count,new_row_o_count,new_col_o_count,'X',finish_state_count+tmp_state,all_char_count-1,start_state)
                        tmp_res.append(res)
                    if pop_char=='X' and board[irow][icol]=='X':
                        trigger+=1
                        new_board=deepcopy(board)
                        #去掉O
                        new_board[irow]=new_board[irow][:icol]+' '+new_board[irow][icol+1:]
                        new_row_x_count=deepcopy(row_x_count)
                        new_col_x_count=deepcopy(col_x_count)
                        new_row_o_count=deepcopy(row_o_count)
                        new_col_o_count=deepcopy(col_o_count)
                        new_row_x_count[irow]-=1
                        new_col_x_count[icol]-=1
                        #判断是否为终止状态
                        tmp_state=int(is_finished(new_board,new_row_x_count,new_col_x_count,new_row_o_count,new_col_o_count))
                        print(finish_state_count,start_state)
                        res=recursive(new_board,new_row_x_count,new_col_x_count,new_row_o_count,new_col_o_count,'O',finish_state_count+tmp_state,all_char_count-1,start_state)
                        tmp_res.append(res)
            print(tmp_res)
            return  True if True in tmp_res else False
        if x_count>o_count:
            return recursive(board,self.row_x_count,self.col_x_count,self.row_o_count,self.col_o_count,'X',start_state,all_char_count,start_state)
        else:

            return recursive(board,self.row_x_count,self.col_x_count,self.row_o_count,self.col_o_count,'O',start_state,all_char_count,start_state)





                         



            







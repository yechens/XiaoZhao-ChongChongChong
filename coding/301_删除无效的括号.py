"""
题目描述：
删除最小数量的无效括号，使得输入的字符串有效，返回所有可能的结果。

说明: 输入可能包含了除 ( 和 ) 以外的字符。

示例 1:

输入: "()())()"
输出: ["()()()", "(())()"]
示例 2:

输入: "(a)())()"
输出: ["(a)()()", "(a())()"]
示例 3:

输入: ")("
输出: [""]

解题思路：
使用BFS的方法，遍历该层每个元素删除一个char的情况，直到某一层出现了正确的字符串。
使用set()减少重复判断。只有删除了"()"中的一个符号，遍历才继续，否则结束！
例如：
第一层：()()
第二层：)()   (()   ())    ()(
第三层：...


"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        #TODO
        #回溯法,DFS

        #BFS
        #判断是否是有效字符
        def is_valid(s):
            left_count=0
            right_count=0
            for ichar in s:
                if ichar=='(':
                    left_count+=1
                if ichar==')':
                    right_count+=1
                if right_count>left_count:
                    return False
            return left_count==right_count
        queue=[s]
        #初始状态判断
        have_valid=is_valid(s)
        count=[] if not have_valid else [s]
        while not have_valid and queue:
            tmp_l=len(queue)
            tmp_queue=set()
            for i_i in range(tmp_l):
                #易错点：pop(0)不是pop(i_i)
                tmpnode=queue.pop(0)
                len_i_s=len(tmpnode)
                for i_index in range(len_i_s):
                    #移除一个char
                    if tmpnode[i_index] in '()':
                        tmp_queue.add(tmpnode[:i_index]+tmpnode[i_index+1:])
            queue=list(tmp_queue)
            #判断有没有符合条件的
            for iq in queue:
                if is_valid(iq):
                    count.append(iq)
                    have_valid=True        
                
        return count









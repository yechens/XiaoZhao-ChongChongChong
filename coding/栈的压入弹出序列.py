'''
题目描述：
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如，序列 {1,2,3,4,5} 是某栈的压栈序列，序列 {4,5,3,2,1} 是该压栈序列对应的一个弹出序列，但 {4,3,5,1,2} 就不可能是该压栈序列的弹出序列。

 

示例 1：

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
示例 2：

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

解体思路：

按pop顺序弹出栈，查看是否能够满足条件

'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        #按pop序列弹出
        newpush=[]
        newpop=[]
        i=0
        j=0
        for inum in pushed:
            #头部
            if inum==popped[0]:
                popped.pop(0)
                #判断之前的是不是一样的
                tmplen=len(newpush)
                for tmpi in range(tmplen-1,-1,-1):
                    if  len(popped)>0 and  newpush[tmpi]==popped[0]:
                        popped.pop(0)
                        newpush.pop(-1)
                    else:
                        break
            else:
                newpush.append(inum)
        #剩下的全部弹出
        print(newpush,popped)
        newpush.reverse()
        for i,j in zip(newpush,popped):
            if i!=j:
                return False
        return True

'''
题目描述：
给出方程式 A / B = k, 其中 A 和 B 均为用字符串表示的变量， k 是一个浮点型数字。根据已知方程式求解问题，并返回计算结果。如果结果不存在，则返回 -1.0。

示例 :
给定 a / b = 2.0, b / c = 3.0
问题: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
返回 [6.0, 0.5, -1.0, 1.0, -1.0 ]

输入为: vector<pair<string, string>> equations, vector<double>& values, vector<pair<string, string>> queries(方程式，方程式结果，问题方程式)， 其中 equations.size() == values.size()，即方程式的长度与方程式结果长度相等（程式与结果一一对应），并且结果值均为正数。以上为方程式的描述。 返回vector<double>类型。

基于上述例子，输入如下：

equations(方程式) = [ ["a", "b"], ["b", "c"] ],
values(方程式结果) = [2.0, 3.0],
queries(问题方程式) = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]. 
输入总是有效的。你可以假设除法运算中不会出现除数为0的情况，且不存在任何矛盾的结果。

解题思路：
    （带权重的）并查集（可重复利用当前模板类）

#几个特例：
#1.两个子图合并，除数是子图的根节点！！！===》 遍历当前除数的子节点，更新权重
#[["a","b"],["e","f"],["b","e"]] 
# a       e       b
#  \       \       \
#    b      f       e
#2.[["a","e"],["b","e"]]
#当前输入的除数，已经是某一个节点的除数了！！！=====》调整除数和被除数的位置，还有weight取倒数
#a    b
# \    \ 
#  e    e
'''

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #并查集
        class deset():
            def __init__(self,all_sen):
                self.all_sen=set(all_sen)
                self.sentence_map={isen:i_index for i_index,isen in enumerate(all_sen)}
                self.parent=[-1]*len(self.sentence_map)
                #权重
                self.parent_weight=[1]*len(self.sentence_map)
            def findparent(self,x):
                if self.parent[x]==-1:
                    return x
                if x==self.parent[x]:
                    return x
                px=self.findparent(self.parent[x])
                return px
            def union(self,x,y,weight):
                x=self.sentence_map[x]
                y=self.sentence_map[y]
                x1=self.findparent(x)
                y1=self.findparent(y)
                #考虑y同时为两个数的除数
                if y1!=y:
                    #反过来
                    x,y=y,x
                    x1,y1=y1,x1
                    weight=1/weight

                if y1==x1:
                    pass
                else:
                    self.parent[y1]=x1
                    self.parent_weight[y]=weight*self.parent_weight[x]
                    #更新以y1为根节点的子图
                    for ison,ipar in enumerate(self.parent):
                        if (y1)==(ipar) and ison!=y1:
                            self.parent_weight[ison]=self.parent_weight[ison]*self.parent_weight[ipar]

        all_sen=set()
        for ia,ib in equations:
            all_sen.add(ia)
            all_sen.add(ib)
        adeset=deset(all_sen)

        for atu,aval in zip(equations,values):
            adeset.union(atu[0],atu[1],aval)
        #判断
        res=[]
        for ia,ib in queries:
            if ia not in all_sen or ib not in all_sen:
                res.append(-1)
                continue
            father_a=adeset.findparent(adeset.sentence_map[ia])
            father_b=adeset.findparent(adeset.sentence_map[ib])
            if father_a!= father_b:
                res.append(-1)
                continue
            #找到权重
            we_ia=adeset.parent_weight[adeset.sentence_map[ia]]
            we_ib=adeset.parent_weight[adeset.sentence_map[ib]]

            res.append(1/(we_ia)*(we_ib))
        return res

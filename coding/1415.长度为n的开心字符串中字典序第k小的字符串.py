'''
题目描述：
一个 「开心字符串」定义为：

仅包含小写字母 ['a', 'b', 'c'].
对所有在 1 到 s.length - 1 之间的 i ，满足 s[i] != s[i + 1] （字符串的下标从 1 开始）。
比方说，字符串 "abc"，"ac"，"b" 和 "abcbabcbcb" 都是开心字符串，但是 "aa"，"baa" 和 "ababbc" 都不是开心字符串。

给你两个整数 n 和 k ，你需要将长度为 n 的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 n 的开心字符串少于 k 个，那么请你返回 空字符串 。

 

示例 1：

输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。
示例 2：

输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。
示例 3：

输入：n = 3, k = 9
输出："cab"
解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"
示例 4：

输入：n = 2, k = 7
输出：""
示例 5：

输入：n = 10, k = 100
输出："abacbabacb"
 

提示：

1 <= n <= 10
1 <= k <= 100


解题思路：
按排列顺序 DFS/递归
注意：递归的终止条件，防止超时



'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        #判断有无可能
        fin_res_count=3
        import copy
        tmpn=n-1
        while tmpn>0:
            fin_res_count*=2
            tmpn-=1
        if fin_res_count<k:
            return ""
        #递归地按顺序生成k个字符串 
        self.res=[]
        def recursive(right_now_char,rn_str):
            #到了给定的长度
            if len(rn_str)==n and len(self.res)<k:
                self.res.append(rn_str)
            #长度超过的话需要终止
            if len(self.res)==k or len(rn_str)>=n:
                return
            if rn_str[-1]!='a':
                recursive(right_now_char,rn_str+'a')
            if rn_str[-1]!='b':
                recursive(right_now_char,rn_str+'b')
            if rn_str[-1]!='c':    
                recursive(right_now_char,rn_str+'c')
        recursive('',"a")
        recursive('',"b")
        recursive('',"c")
        #生成过程中存在第k个就输出，否则输出空
        if len(self.res)>=k:
            return self.res[-1]
        else:
            return ""



                
                




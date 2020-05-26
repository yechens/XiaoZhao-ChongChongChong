'''
题目描述：
给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。

'?' 可以匹配任何单个字符。
'*' 可以匹配任意字符串（包括空字符串）。
两个字符串完全匹配才算匹配成功。

说明:

s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
示例 1:

输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
示例 2:

输入:
s = "aa"
p = "*"
输出: true
解释: '*' 可以匹配任意字符串。
示例 3:

输入:
s = "cb"
p = "?a"
输出: false
解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
示例 4:

输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
示例 5:

输入:
s = "acdcb"
p = "a*c?b"
输出: false

解题思路：
1.dp[i][j]:表示字符串s到i位置能否和字符串p到j位置 这两个子字符串能否匹配
2.base case 需要考虑*的出现
3.dp[i][j]由dp[i-1][j-1],dp[i][j-1],dp[i-1][j]三个位置的值获得：
    dp[i-1][j-1]==True时，s[i]和p[i]相等或者有一个为* 或者？就是True
    dp[i][j-1]或,dp[i-1][j] 为True的情况下，s[i]和p[i]有一个为* ，即为True
4.易错点：
    不用写else，默认为false
    当前s,p对应位置有一个为*即可，而不是只有其中一个为*（参见代码）
5.TODO：
    时间复杂度优化
    回溯法



'''




class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #dp:
        tmp=p
        p=s
        s=tmp
        dp=[[False for _ in range(len(s)+1)] for _ in range(len(p)+1)]
        #base case
            #对s
        dp[0][0]=True
        for i_index,ichar_s in enumerate(s):
            i_index+=1
            dp[0][i_index]= True if dp[0][i_index-1] and ichar_s=='*' else False
            #对p
        for i_index,ichar_p in enumerate(p):
            i_index+=1
            dp[i_index][0]= True if dp[i_index-1][0] and ichar_p=='*' else False
        #递推
        for irow in range(1,len(p)+1):
            for icol in range(1,len(s)+1):

                #易错点：不用写else，默认为false
                #左上对角为True
                if dp[irow-1][icol-1] :
                    if p[irow-1]==s[icol-1] \
                    or p[irow-1]=='?' or s[icol-1]=='?' or \
                    p[irow-1]=='*' or s[icol-1]=='*':
                        #当前元素值相同
                        dp[irow][icol]=True
                
                #非左上角，但是相邻行或者列为True，则必有“*”
                if dp[irow][icol-1]:
                    #易错点：当前s,p对应位置有一个为*即可，而不是只有其中一个为*
                    if s[icol-1]=='*' or p[irow-1]=='*':
                        dp[irow][icol]= True  
                if dp[irow-1][icol]:
                    #易错点：当前s,p对应位置有一个为*即可，而不是只有其中一个为*
                    if p[irow-1]=='*' or s[icol-1]=='*':
                        dp[irow][icol]= True 
        #for icol in dp:
        #    print(icol)
        return dp[-1][-1]








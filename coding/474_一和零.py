'''
题目描述：
在计算机界中，我们总是追求用有限的资源获取最大的收益。

现在，假设你分别支配着 m 个 0 和 n 个 1。另外，还有一个仅包含 0 和 1 字符串的数组。

你的任务是使用给定的 m 个 0 和 n 个 1 ，找到能拼出存在于数组中的字符串的最大数量。每个 0 和 1 至多被使用一次。

注意:

给定 0 和 1 的数量都不会超过 100。
给定字符串数组的长度不会超过 600。
示例 1:

输入: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
输出: 4

解释: 总共 4 个字符串可以通过 5 个 0 和 3 个 1 拼出，即 "10","0001","1","0" 。
示例 2:

输入: Array = {"10", "0", "1"}, m = 1, n = 1
输出: 2

解释: 你可以拼出 "10"，但之后就没有剩余数字了。更好的选择是拼出 "0" 和 "1" 。

解题思路：
dp:

dp[i][j]表示容量为i,j时能容纳的数的个数

转移方程：dp[i][j]=max(dp[i][j],dp[i-zc][j-oc]+1)
'''


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        #DP
        #dp[i][j]表示容量为i,j时能容纳的数的个数
        #右下到左上遍历
        dp=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for istr in strs:
            zc=istr.count('0')
            oc=istr.count('1')
            for i in range(m,zc-1,-1):
                for j in range(n,oc-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-zc][j-oc]+1)
        return dp[-1][-1]






        #TODO 能否优化该代码
        #dp[i]表示从起始到该位置能拼出的最多字符串，同时剩余的字符串的数量，tuple
        dp=[0]*len(strs)
        #原str计数
        count_str=[]
        for istr in strs:
            izero=0
            ione=0
            for ichar in istr:
                if ichar==0:
                    izero+=1
                if ione==0:
                    ione+=1
            count_str.append((izero,ione))
        #判断
        def isok(i):
            if count_str[i][0]<=m and count_str[i][1]<=n:
                return True
            else:
                return False
        #base case
        
        dp[0]=(1,m-count_str[0][0],n-count_str[0][1])if isok(0)  else (0,0,0)
        #遍历
        res=dp[0][0]
        for i in range(1,len(strs)):
            izero,ione=count_str[i]
            if not isok(i):
                dp[i]=(0,0,0)
                continue
            max_count=1
            zc=izero
            oc=ione
            for j in range(0,i):
                if dp[j][1]+izero<=m and dp[j][2]+ione<=n:
                    if dp[j][0]+1>max_count:
                        max_count=dp[j][0]+1
                        zc=dp[j][1]+izero
                        oc=dp[j][2]+ione
                    #if dp[j][0]+1==max_count and

            dp[i]=(max_count,zc,oc)
            if dp[i][0]>res:
                res=dp[i][0]
        return res


                



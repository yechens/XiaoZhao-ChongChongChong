'''
题目描述：
这里有 d 个一样的骰子，每个骰子上都有 f 个面，分别标号为 1, 2, ..., f。

我们约定：掷骰子的得到总点数为各骰子面朝上的数字的总和。

如果需要掷出的总点数为 target，请你计算出有多少种不同的组合情况（所有的组合情况总共有 f^d 种），模 10^9 + 7 后返回。

 

示例 1：

输入：d = 1, f = 6, target = 3
输出：1
示例 2：

输入：d = 2, f = 6, target = 7
输出：6
示例 3：

输入：d = 2, f = 5, target = 10
输出：1
示例 4：

输入：d = 1, f = 2, target = 3
输出：0
示例 5：

输入：d = 30, f = 30, target = 500
输出：222616187
 

提示：

1 <= d, f <= 30
1 <= target <= 1000

解题思路：
DP：
dp[i][j]表示仍i个骰子和为j的组合数量
转移方程：dp[i][j]=sum(dp[i-1][j-k])(k=1,2,..,f)
关键点：base case dp[1]的初始化，dp[1]的最大和只能为min(f,target)


'''




class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        #dp[i][j]表示仍i个骰子和为j的组合数量
        #dp[i][j]=sum(dp[i-1][j-k])(k=1,2,..,f)
        dp=[[0 for _ in range(target+1)] for _ in range(d+1)]
        #base case 只到min(f, target)
        dp[1][1:min(f, target)+1]=[1]*(min(f, target))
        for i in range(2,d+1):
            #j不可能小于i
            for j in range(i,target+1):
                for k in range(1,f+1):
                    if k>=j:break
                    #(A + B) mod M = (A mod M + B mod M) mod M
                    dp[i][j]=(dp[i][j]+dp[i-1][j-k])%(10**9+7)
                
        return dp[d][target]#%(10**9+7)

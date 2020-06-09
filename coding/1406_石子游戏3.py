'''
题目描述：
Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 stoneValue 给出。

Alice 和 Bob 轮流取石子，Alice 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 1、2 或 3 堆石子 。比赛一直持续到所有石头都被拿走。

每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 0 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。

假设 Alice 和 Bob 都采取 最优策略 。如果 Alice 赢了就返回 "Alice" ，Bob 赢了就返回 "Bob"，平局（分数相同）返回 "Tie" 。

 

示例 1：

输入：values = [1,2,3,7]
输出："Bob"
解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。
示例 2：

输入：values = [1,2,3,-9]
输出："Alice"
解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。
示例 3：

输入：values = [1,2,3,6]
输出："Tie"
解释：Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。
示例 4：

输入：values = [1,2,3,-1,-2,-3,7]
输出："Alice"
示例 5：

输入：values = [-1,-2,-3]
输出："Tie"
 

提示：

1 <= values.length <= 50000
-1000 <= values[i] <= 1000

解题思路：
关键是DP的表示:dp[i]表示当前位置起手能够取得（包含后续操作）的最高分数

举个🌰：
   1  2  3  7
dp          7
dp       10 7
dp    12 10 7
dp 6  12 10 7
sum=13
dp[0]=6
Bob赢

易错点：
当步长+当前位置i,超过最后一个位置时，当前i位置可以获取位置i到最后位置的所有分数

'''



class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        #dp
        #重要！！！dp[i]表示当前位置起手能够取得（包含后续操作）的最高分数
        #从后往前 遍历
        #先不需要管是谁 
        sum_point=0
        dp=[float('-inf')]*len(stoneValue)
        #最后一个位置
        dp[-1]=stoneValue[-1]
        for i in  range(len(stoneValue)):
            i=len(stoneValue)-i-1
            sum_point+=stoneValue[i]
            #最后一个位置，直接跳过
            if i==len(stoneValue)-1:
                continue
            #sum_point-(0 if i+j >len(stoneValue)-1 else dp[i+j])表示下一步对手能获取的分数
            #当前位置到最后位置的总分减去对手（下一步）能够获取的分就为自己能够获得分数
            for j in  [1,2,3]:
                #sum_point-(0 if i+j >len(stoneValue)-1 else dp[i+j]\
                #表示当步长+当前位置i,超过最后一个位置时，当前i位置可以获取位置i到最后位置的所有分数
                dp[i]=max(dp[i],sum_point-(0 if i+j >len(stoneValue)-1 else dp[i+j]) )
        #print(dp)
        if (sum_point-dp[0])==dp[0]:
            return 'Tie'
        else:
            return 'Bob'if (sum_point-dp[0])>dp[0]  else 'Alice'
            




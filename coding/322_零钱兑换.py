"""
题目描述：
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

示例：
示例 1:

输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
示例 2:

输入: coins = [2], amount = 3
输出: -1

说明:
你可以认为每种硬币的数量是无限的。

解题思路：
这个无限背包问题的状态应该是背包容量，即硬币组成的数目，选择为每种硬币选x个，这样去做状态转移未免偏复杂，因此可以考虑组成数目i所需的硬币数量=组成数目i-coins[j]+1中的最小值，
状态转移方程为dp[i] = min(dp[i-coins[0], dp[i-coins[1]...]])
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        dp = [float('inf') for i in range(amount+1)]
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        return dp[amount] if dp[amount]!=float('inf') else -1

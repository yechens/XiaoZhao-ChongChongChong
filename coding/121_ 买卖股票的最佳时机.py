class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        
        dp_i_0 = 0 # 第 i 天没有持股
        dp_i_1 = -float('inf') # 第 i 天持有股票，一开始初始化为负无穷(第0天)
        for p in prices:
            dp_i_0 = max(dp_i_0, dp_i_1 + p)
            # 注意！因为只允许走一次交易，所以隐状态中有 k=1 的约束
            # k = 0 表示不允许有任何交易
            # dp[i][0][0] = 0, dp[i][0][1] = -inf
            dp_i_1 = max(dp_i_1, 0-p)
            # 如果不限制交易次数，则 dp_i_1 更新为:
            # dp_i_1 = max(dp_i_1, dp_i_0 - p)
        print(dp_i_0, dp_i_1)
        return dp_i_0
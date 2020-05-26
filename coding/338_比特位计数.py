"""
题目描述：
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。

示例：
示例 1:

输入: 2
输出: [0,1,1]
示例 2:

输入: 5
输出: [0,1,1,2,1,2]

题解：
正常的解法中需要注意的是按位与&，移位操作>>=1
DP解法中num为2**n时，二进制为100... 1的个数为num-2**n的1的个数+1,从2**n ~ 2**(n+1)之间的数的1的个数均可以这样算出来，遍历一次即可，时间复杂度为O(n)
"""
#正常的位运算解法
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for i in range(num+1)]
        # print(dp)
        for n in range(1, num+1):
            dp[n] = self.helper(n)
        # print(dp)
        return dp

    def helper(self, num):
        count = 0
        while num > 0:
            if num & 1 == 1:
                count += 1
            num >>= 1
        return count

#DP解法
class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0 for i in range(num+1)]
        if num>=1:
            dp[1] = 1
        t = 1
        for i in range(2, num+1):
            dp[i] = dp[i-2**t] + 1
            if i == 2**(t+1)-1:
                t += 1
        return dp

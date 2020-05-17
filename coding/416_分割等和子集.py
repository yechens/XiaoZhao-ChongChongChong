"""
题目描述：
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200
示例 1:

输入: [1, 5, 11, 5]

输出: true

解释: 数组可以分割成 [1, 5, 5] 和 [11].
 

示例 2:

输入: [1, 2, 3, 5]

输出: false

解释: 数组不能分割成两个元素和相等的子集.

解题思路：
1.问题转化：把两个数组和是否相等的问题转化为“寻找一个能够和等于某个数的子序列”
2.关键点：
    dp数组如何构建：
    考虑到遍历时，可能会有对每个位置的数可以选择使用或者不使用，如果使用暴力解法，必然超时。
    因此，需要寻找“相对变化不大的值”——子序列的和（和的数量远小于“选择和不选择”的这种方式）
3.操作流程：
    遍历nums的每个数时，只需要加上之前数能够得到的和，就可以得到新的能够获取到的和的状态。最后判断能够等于某个所需值即可！（具体操作看下述代码解释）

"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2!=0:
            return False
        #判断是否有和为split_sum的子数组
        split_sum=sum(nums)//2
        #dp[j]子序列和能否等于j<===上一个数和的状态
        dp=[False for _ in range(split_sum+1)]
        #new_dp当前数的和的状态
        new_dp=[False for _ in range(split_sum+1)]
        dp[0]=True
        for i in  range(len(nums)):
            i+=1
            #易错点：
            #当前值大于spilt_sum时也可以不操作
            #需记录到上一个数的序列能够得到的所有和（对应标True）
            #至少两行数组保存状态
            for j in range(split_sum+1):
                if dp[j]:
                    if (j+nums[i-1])>split_sum:
                        continue
                    else:
                        new_dp[j]=True
                        new_dp[j+nums[i-1]]=True
            #更新dp的状态
            dp=new_dp
            new_dp=[False for _ in range(split_sum+1)]
            if dp[split_sum]:
                return True
        return False


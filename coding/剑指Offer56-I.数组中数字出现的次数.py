'''
题目描述:
一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。要求时间复杂度是O(n)，空间复杂度是O(1)。

 

示例 1：

输入：nums = [4,1,4,6]
输出：[1,6] 或 [6,1]
示例 2：

输入：nums = [1,2,10,4,1,4,3,3]
输出：[2,10] 或 [10,2]
 

限制：

2 <= nums.length <= 10000

解题思路:
方法：数字的位操作——巧分组
-考虑一个整型数组 nums 里除1个数字之外，其他数字都出现了两次，
-结果是所有数字异或即为唯一的那个数字
-本题考虑把数字分成两个子数组，每个数组包含唯一的那个数字
-由于所有数的异或结果肯定不为0，故找到以后结果数中不为0的位置，进行划分（相同数字同一位置必相同，而异或结果对应位置不同）

'''

class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        #巧分组
        #所有数异或
        allexo=nums[0]
        for i in range(1,len(nums)):
           allexo^=nums[i]
        #根据异或结果分组
        #找到分组的位置
        res=1
        while res&allexo==0:
            res<<=1
        a,b=0,0#与0异或为数字本身
        #找到a,b
        for i in range(len(nums)):
            if nums[i]&res==0:
                #确定位置不同
                a^=nums[i]
            else:
                b^=nums[i]
        return [a,b]





        
         

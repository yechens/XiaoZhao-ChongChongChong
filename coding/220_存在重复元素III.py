'''
题目描述：
在整数数组 nums 中，是否存在两个下标 i 和 j，使得 nums [i] 和 nums [j] 的差的绝对值小于等于 t ，且满足 i 和 j 的差的绝对值也小于等于 ķ 。

如果存在则返回 true，不存在返回 false。

 

示例 1:

输入: nums = [1,2,3,1], k = 3, t = 0
输出: true
示例 2:

输入: nums = [1,0,1,1], k = 1, t = 2
输出: true
示例 3:

输入: nums = [1,5,9,1,5,9], k = 2, t = 3
输出: false

解体思路：

方法一：暴力递归-最后一个例子超时
方法二：桶
1.使用商作为该元素的桶编号（同一桶内必满足 t条件）
2.桶只保留k个元素，多的pop（满足k条件）
3.某一数的判断是，该数对应的桶有没有元素，以及前一个及后一个桶中有没有满足t条件的元素

'''

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        
        #桶
        if t < 0 or k < 0:
            return False
        self.res=False
        self.bucket={}
        #尺寸 保证t
        size=t+1
        for i in range(len(nums)):
            #注意：商不是余数
            bucket_index=nums[i]//(size)
            if bucket_index in  self.bucket:
                return True
            self.bucket[bucket_index]=nums[i]
            #可能在前一个也可能在后一个
            if bucket_index-1 in self.bucket and abs(self.bucket[bucket_index-1]-nums[i])<=t:
                return True
            if bucket_index+1 in self.bucket and abs(self.bucket[bucket_index+1]-nums[i])<=t:
                return True
            #保持只有k个，每个桶只有一个元素
            if i>=k:
                self.bucket.pop(nums[i-k]//size)
        return False
                



        
        return self.res
        
        
        #暴力法--最后一个例子超时
        self.res=False
        def recursive(nums,pos1,pos2,k,t):
            #pos1<pos2
            if pos2>=len(nums):
                return
            if pos1==pos2:
                recursive(nums,pos1,pos2+1,k,t)
                return 
            #满足条件
            if abs(pos1-pos2)<=k and abs(nums[pos1]-nums[pos2])<=t:
                self.res=True
                return 
            if abs(pos1-pos2)<=k:
                recursive(nums,pos1,pos2+1,k,t)
                #易错点：别忘了小于的情况 pos1+1这一情况也需要考虑
                recursive(nums,pos1+1,pos2,k,t)
            else:
                recursive(nums,pos1+1,pos2,k,t)
        recursive(nums,0,1,k,t)
        return self.res
            

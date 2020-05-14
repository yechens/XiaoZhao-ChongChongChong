class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #dp
        max_num_list=[nums[0]]
        rn_maxnum=nums[0]
        for iindex,inum in enumerate(nums[1:]):
            max_num_list.append(max(inum,inum+max_num_list[iindex]))
        return max(max_num_list)
        
        #1st stage
        presum=nums[0]
        res=nums[0]
        for inum in nums[1:]:
            if presum<0:
                presum=inum
            else:
                presum+=inum
            res=max(presum,res)
        return res

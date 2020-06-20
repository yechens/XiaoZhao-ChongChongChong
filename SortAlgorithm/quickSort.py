import random

def quickSort(nums, left, right):
    """分治法
    """
    if left >= right:
        return 
    low, high = left, right
    # tmp = nums[left] # 这里相当于随机选择一个数，最终tmp一定是在排好序后的位置上
    # 可以尽可能地避免时间复杂度为O(n^2)的情况出现
    tmp = random.choice(nums)
    nums[left], tmp = tmp, nums[left]
    while left < right:
        while left < right and nums[right] >= tmp:
            right -= 1
        nums[left], nums[right] = nums[right], nums[left]
        while left < right and nums[left] < tmp:
            left += 1
        nums[left], nums[right] = nums[right], nums[left]
    nums[left] = tmp
    # 递归对 k 的左半边和右半边进行递归排序
    quickSort(nums, low, left - 1)
    quickSort(nums, left + 1, high)

# Test
nums = [-10, -1, 100, 0, 18, 7, 2, -5, -1000]
quickSort(nums, 0, len(nums) - 1)
print(nums) # [-1000, -10, -5, -1, 0, 2, 7, 18, 100]

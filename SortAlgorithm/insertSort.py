import random

def insertSort(nums):
    """(直接)插入排序不改变数组的相对顺序，所以是稳定的排序算法
       时间复杂度：O(n^2)
    """
    n = len(nums)
    if not nums:
        return
    for i in range(1, n): # 原地排序
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = key

# Test
nums = [10, 0, -1, 5, 9, 7]
insertSort(nums)
print(nums) # [-1, 0, 5, 7, 9, 10]


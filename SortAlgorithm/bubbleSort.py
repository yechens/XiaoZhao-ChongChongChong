"""
对数组nums原地进行冒泡排序
"""

def bubbleSort(nums):
    n = len(nums)
    for i in range(n - 1):
        count = 0
        for j in range(n - i - 1):
            if nums[j] > nums[j+1]: # 按升序排序，原地置换
                nums[j], nums[j+1] = nums[j+1], nums[j]
                count += 1
        if count == 0:
            break
    # 原地排序，不需要返回
    
nums = [-10, -1, 100, 0, 18, 0, 0, 7, 2, -5, -1000]
# Test
bubbleSort(nums)
print(nums) # [-1000, -10, -5, -1, 0, 0, 0, 2, 7, 18, 100]

'''
对数组 nums 进行原地二路归并排序
''' 

def merge(nums, start, mid, end):
    """对nums数组进行原地归并排序
    """
    l1 = mid - start + 1 # [start, mid]
    l2 = end - mid # [mid+1, end)
    tmp1, tmp2 = [], [] # 原地排序需要开辟额外的存储空间
    for i in range(l1):
        tmp1.append(nums[start + i]) # 注意！这里是 start + i（与 start 有关）
    for j in range(l2):
        tmp2.append(nums[mid + 1 + j])
    i, j = 0, 0
    for k in range(start, end + 1): # end 可以取到
        if j >= l2 or (i < l1 and tmp1[i] <= tmp2[j]):
            nums[k] = tmp1[i]
            i += 1
        else:
            nums[k] = tmp2[j]
            j += 1
#     return nums # 原地排序，不需要返回

def mergeSort(nums, start, end):
    """对nums数组进行递归切割
    """
    if start < end:
        mid = start + (end - start) // 2 # 数组中点
        mergeSort(nums, start, mid)
        mergeSort(nums, mid+1, end)
        # 归并排序
        merge(nums, start, mid, end)
        
# test        
nums = [100, -1, 0, 18, 2, 7, -5]
mergeSort(nums, 0, len(nums) - 1)
print(nums) # [-5, -1, 0, 2, 7, 18, 100]

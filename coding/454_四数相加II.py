'''
题目描述：
给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0

解题思路：
A-B 遍历求和sumab
C-D 遍历求和sumcd

查看sumcd中的和的相反数-icd，在sumab中有无，有则说明能够加和为0



'''

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        if len(A)==0:
            return 0
        #方法1:
        res=0
        sum_a_b={}
        for ia in A:
            for ib in B:
                sum_a_b[ia+ib]=sum_a_b.get(ia+ib,0)+1
        sum_c_d={}
        for ic in C:
            for id_ in D:
                #查看sum_c_d有无sum_a_b的相反数
                if -(ic+id_) in sum_a_b.keys():
                    res+=sum_a_b[-(ic+id_)]

        return res
        
        

        
        
        #方法2:超时
        sum_a_b={}
        for ia in A:
            for ib in B:
                sum_a_b[ia+ib]=sum_a_b.get(ia+ib,0)+1
        sum_c_d={}
        for ic in C:
            for id_ in D:
                sum_c_d[ic+id_]=sum_c_d.get(ic+id_,0)+1
        #剪枝
        eff_sum_max=max(max(sum_a_b.keys()),max(sum_c_d.keys()))
        eff_sum_min=min(min(sum_a_b.keys()),min(sum_c_d.keys()))
        eff_sum_max=min(abs(eff_sum_max),abs(eff_sum_min))
        eff_sum_min=-eff_sum_max
        #求和
        res=0
        for isumab,countab in sum_a_b.items():
            if isumab>=eff_sum_min and isumab<=eff_sum_max:
                for isumcd,countcd in sum_c_d.items():
                    if isumcd>=eff_sum_min and isumcd<=eff_sum_max:
                        if isumab+isumcd==0:
                            res+=countab*countcd
        return res

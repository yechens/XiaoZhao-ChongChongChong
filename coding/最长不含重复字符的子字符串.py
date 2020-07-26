'''
题目描述:
请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。

 

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


解题思路:
双指针 ----若有重复first_pointer,move到等于当前值的数的下一个

'''


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #code 简化版（但时间复杂度高一点） 双指针
        first=0
        res=0
        for i_index,ichar in enumerate(s):
            if ichar in s[first:i_index]:
                #移动到等于当前值的数的下一个
                while s[first]!=ichar:
                    first+=1
                #下一个
                first+=1
            else:
                res=max(res,i_index-first+1)
        return res


                
        
        
                
                
                
        









        #双指针 有个性质 某个字符串包含重复字符串 则包含该字符串的字符串一定包含重复字符串
        if not s:return 0
        i=0
        j=-1
        tmpdict={}
        res=0
        for i_index,inum in enumerate(s):
            if tmpdict.get(inum,0)==0:
                tmpdict[inum]=1
                j=i_index
                res=max(res,j-i+1)
            else:
                tmpdict[inum]+=1
                #找到下一个不重复的子串
                while s[i]!=inum:
                    tmpdict[s[i]]-=1
                    i+=1
                tmpdict[s[i]]-=1
                #res=max(res,j-i)
                i+=1
            
        return res

'''
题目描述：
给定一个字符串数组，将字母异位词组合在一起。字母异位词指字母相同，但排列不同的字符串。

示例:

输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
输出:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
说明：

所有输入均为小写字母。
不考虑答案输出的顺序。

解题思路：
方法1:每个char计数，判断计数的list是否一样即可
方法2:每个word中char排序，排序后相同的word归为一个list




'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #每个char计数，判断计数的list是否一样即可
        res_dict={}
        for iword in strs:
            count=[0]*26
            for ichar in iword:
                count[ord(ichar)-ord('a')]+=1
            num_str=str(count)
            if num_str not in res_dict:
                res_dict[num_str]=[]
            res_dict[num_str].append(iword)
        return list(res_dict.values())
        #每个word中char排序，排序后相同的word归为一个list
        id2originstr={i_index:iword for i_index,iword in enumerate(strs)} 
        for i_index,iword in enumerate(strs):
           strs[i_index]=''.join(sorted(iword))
        res_dict={}
        for i_index,iword in enumerate(strs):
            if iword not in list(res_dict.keys()):
                res_dict[iword]=[]
            res_dict[iword].append(id2originstr[i_index])
        res=[]
        for val in res_dict.values():
            res.append(val)
        return res
        


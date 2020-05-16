'''
题目描述:
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

解题思路:
    递归判断子字符串是否为回文子串！


'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:return s
        #dp=[[False]*len(s)]*len(s)
        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_len=1
        cur_s=s[0]
        for i in range(len(s)):
            dp[i][i]=True
        for j in range(1, len(s)):
            for i in range(0, j):
                #判断子串是否为回文子串
                if s[i]==s[j]:
                    #小于3的长度则为回文
                    if j-i<3:
                        dp[i][j]=True
                    else:
                        #dp[*][j-1]已经遍历过了
                        dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False
                if dp[i][j]:
                    if max_len<(j-i+1):
                        cur_s=s[i:j+1]
                        max_len=(j-i+1)
        return cur_s


                


                

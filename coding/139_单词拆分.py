"""
题目描述：
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例1:
输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
     注意你可以重复使用字典中的单词。

示例2：
输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

解题思路：
定义一个长度为 n+1 的dp数组：dp=[0,..., 0]，dp[i]表示s的前i位是否可以用wordDictwordDict中的单词表示。
初始化 dp[0] = 1 表示空字符可以被表示。
遍历字符串：
  - 第一层循环 i，遍历字符串的所有子串，遍历区间:[0, n)
  - 第二层循环 j，遍历区间: [i+1, n]
  状态转移：若 dp[i]==1 且 s[i:j] 在单词列表中 => dp[j] = 1 说明：dp[i]==1说明s的前i位可以用字典表示，如果s[i:j]在字典中，说明前j位也可以被字典表示。最终 dp[n] 的结果即代表字符串s是否可以用字典中的单词表示

"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(n):
            for j in range(i+1, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = 1
            print(dp)
        return dp[n] == 1

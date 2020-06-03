"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:
输入: "hello"
输出: "holle"

示例 2:
输入: "leetcode"
输出: "leotcede"

说明:
元音字母不包含字母"y"

解题思路：
双指针分别从首尾开始遍历；注意遍历条件：i < j 
"""
class Solution:
    def reverseVowels(self, s: str) -> str:

        if not s: return ""

        i, j = 0, len(s) - 1
        s = [c for c in s] # str -> list
        # 元音字母可能是大写 / 小写
        t = {'a','e','i','o','u','A','E','I','O','U'}
        while i < j:
            # print(i, j)
            while i < j and s[i] not in t: i += 1
            while i < j and s[j] not in t: j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1

        return ''.join(s)

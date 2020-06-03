'''
题目描述：
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

示例:

s = "3[a]2[bc]", 返回 "aaabcbc".
s = "3[a2[c]]", 返回 "accaccacc".
s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".

解题思路：
1.设置栈stack，遍历s
2.遍历过程中，判断当前字符串是不是']'
 2.1不是则入栈
 2.2是则出栈直到找到'['
 2.3找到当前 [] 层对应的数字
 2.4生成子括号对应的重复子串
 2.5压栈
3.''.join(stack)
点：
字符串逆序：s[::-1]
易错点：
数字可能有多位数

'''

class Solution:
    def decodeString(self, s: str) -> str:
        #stack
        stack=[]
        for ichar in s:
            #出栈
            if ichar==']':
                tmpstr=''
                #点：tmpstr加在pop数的右边就不用逆序了
                while stack[-1]!='[':
                    tmpstr=stack.pop()+tmpstr
                #pop'['
                stack.pop()
                #pop数字 易错点：可能有多位数
                times=''
                while stack and stack[-1]>='0' and stack[-1]<='9':
                    times=stack.pop()+times
                new_str=''
                for i in range(int(times)):
                    new_str=new_str+tmpstr
                #压栈回去
                stack.append((new_str))                  
            else:
                stack.append(ichar)
        return ''.join(stack)

            

'''
Problem:

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

'''


class Solution(object):
    def decodeString(self, s):

        n = 0
        digit = 0
        pattern = ''
        stack = []
        for char in s:
            if char.isdigit():
                digit = digit*10 + int(char)
            elif char == "[":
                stack.append(pattern)
                stack.append(digit)
                pattern = ''
                digit = 0
            elif char == "]":
                n = stack.pop()
                prevStr = stack.pop()
                pattern = prevStr+pattern*n
            else:
                pattern += char

        return pattern
        
        
        
        
 class Solution(object):
    def decodeString(self, s):

        n = 0
        start = end = -1
        digit = 0
        stack = []
        for i in range(len(s)):
            if s[i].isdigit():
                digit = digit*10 + int(s[i])
            elif s[i] == "[":
                stack.append(digit)
                stack.append(s[i])
                digit = 0
            elif s[i] == "]":
                pattern = ""
                while stack[-1] != "[":
                    pattern += stack.pop()
                stack.pop()    # pop out "["
                n = int(stack.pop())
                tmp = pattern[::-1]*n
                for c in tmp:
                    stack.append(c)
            else:
                stack.append(s[i])

        return "".join(stack)

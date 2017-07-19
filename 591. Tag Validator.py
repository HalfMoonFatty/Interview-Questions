'''
Problem:

Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

1. The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
2. A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. 
Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. 
A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.
'''


import string
class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """
        def isValidTag(tag, isEnd, hasTag):
            if len(tag) < 1 or len(tag) > 9: return False
            for char in tag:
                if char not in string.ascii_uppercase: return False
            if isEnd:
                if len(stack) and stack[-1] == tag:
                    stack.pop()
                else: return False
            else:
                stack.append(tag)
                hasTag[0] = True
            return True
                
                
        def isValidCdata(cdata):
            return cdata.startswith("[CDATA[") and hasTag[0]


        
        if code[0] != '<' or code[-1] != '>': return False
        
        stack = []
        hasTag = [False]
        
        i = 0
        while i < len(code):
            if len(stack) == 0 and hasTag[0]:
                return False
            if code[i] == '<':
                if code[i+1] == '!':   # cdata
                    closeindex = code.find(']]>', i+1)
                    if closeindex < 0 or not isValidCdata(code[i+2:closeindex]): return False
                elif code[i+1] == '/':  # close tag
                    closeindex = code.find('>', i+1)
                    if closeindex < 0 or not isValidTag(code[i+2:closeindex], True, hasTag): return False
                else: # start tag
                    closeindex = code.find('>', i+1)
                    if closeindex < 0 or not isValidTag(code[i+1:closeindex], False, hasTag): return False
                i = closeindex
            i += 1
                
        return len(stack) == 0 and hasTag[0]
                

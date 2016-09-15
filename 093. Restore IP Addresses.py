'''
Problem:

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

For example:
Given "25525511135",
return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
            :type s: str
            :rtype: List[str]
            """
        def isValid(s):
            if (len(s) == 1 and 0 <= int(s) <10) or (len(s) == 2 and 9 < int(s) < 100) or (len(s) == 3 and 99 < int(s) < 256):
                return True
            else:
                return False

        def getIpAddr(count,s,start,res,result):
            # base
            if count == 3 and isValid(s[start:]):
                result.append(res+s[start:])
                return
            elif count < 3: # note
                for i in range(1,4):
                    if isValid(s[start:start+i]):    # check here
                        getIpAddr(count+1, s, start+i, res+s[start:start+i]+".", result)
                return


        result = []
        getIpAddr(0,s,0,"",result)
        return result

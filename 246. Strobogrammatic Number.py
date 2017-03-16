'''
Problem:

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.
'''


'''
Solution:

Time: O(n)
Space: O(1) (constant)
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
            :type num: str
            :rtype: bool
            """

        mp = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}

        i,j = 0,len(num)-1
        while i <= j:
            if num[i] not in mp or num[j] not in mp:
                return False
            elif mp[num[i]] != num[j] or mp[num[j]] != num[i]:
                return False
            i += 1
            j -= 1
        return True

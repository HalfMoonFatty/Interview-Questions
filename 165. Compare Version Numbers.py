'''
Problem:

Compare two version numbers version1 and version2.
If version1 > version2 return 1, if version1 < version2 return -1, otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering: 0.1 < 1.1 < 1.2 < 13.37

'''

'''
Solution: 2 pointers

Time: O(M+N)
Space: O(M+N)
'''


class Solution(object):
    def compareVersion(self, version1, version2):
        """
            :type version1: str
            :type version2: str
            :rtype: int
            """
        l1 = version1.split('.')
        l2 = version2.split('.')

        i = j = 0

        while i < len(l1) and j < len(l2):
            if int(l1[i]) == int(l2[j]):
                if i == len(l1)-1 and j == len(l2)-1:
                    return 0
                else:
                    i += 1
                    j += 1

            elif int(l1[i]) < int(l2[j]):
                return -1    # early return

            elif int(l1[i]) > int(l2[j]):
                return 1     # early return

        # if l1 has more elements
        while i < len(l1):
            if int(l1[i]) == 0:    # skip '0'
                i+=1
            else:
                return 1

        # if l2 has more elements
        while j < len(l2):
            if int(l2[j]) == 0:    # skip '0'
                j+=1
            else:
                return -1

        return 0

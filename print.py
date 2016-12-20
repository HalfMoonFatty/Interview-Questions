'''
Problem:
    Given an array of n positive integers and a positive integer s, find the minimal length of a subarray of which the sum ≥ s. 
    If there isn't one, return 0 instead.
    For example, given the array [2,3,1,2,4,3] and s = 7,
    the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
    If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''


'''
Solution: 快慢指针
Time: O(n)
Space: O(1)
'''

class Solution:

    def minimumSize(self, nums, s):
        if not nums: return -1

        minSize = sys.maxint  
        sum = 0
        i = 0
        for j in range(len(nums)):
            sum += nums[j]
            if sum >= s:
                while i <= j: # try to shrink the current minSize
                    if sum -nums[i]< s:
                        break
                    sum -= nums[i]
                    i += 1  
                minSize = min(minSize, j-i+1)    # update minSize

        return minSize if minSize <= len(nums) else -1
        
       
       

'''
Problem:
Given a string, find the length of the longest substring without repeating characters. 
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
For "bbbbb" the longest substring is "b", with the length of 1.
'''


# Time: O(n)
# Space:O(n)


class Solution:

    def lengthOfLongestSubstring(self, s):

        if not s or len(s) < 1:
            return 0

        j = 0
        charset = sets.Set()
        maxLen = -1

        for i in range(len(s)):  # 慢
            while j < len(s) and not s[j] in charset:  # 快 note: j < len(s)
                charset.add(s[j])
                j += 1
            maxLen = max(maxLen,j-i)
            charset.remove(s[i])
        return maxLen

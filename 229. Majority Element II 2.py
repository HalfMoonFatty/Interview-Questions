http://www.geeksforgeeks.org/given-an-array-of-of-size-n-finds-all-the-elements-that-appear-more-than-nk-times/


class Solution(object):
    def majorityElement(self, nums):
        """
            :type nums: List[int]
            :rtype: List[int]
            """
        def KmajorityElem(nums, k):
            if not nums or len(nums) < k:
                return list(set(nums))
    
            candidatelist = []
            candidates = {}
            for n in nums:
                if n in candidatelist:
                    candidates[n] += 1
                else:
                    if len(candidatelist) < k: # candidates is not full
                        candidatelist.append(n)
                        candidates[n] = 1
                    else:
                        for c in candidatelist:
                            candidates[c] -= 1
                            if candidates[c] == 0:
                                candidatelist.remove(c)
            
                
            res = []
            for elem in candidatelist:
                count = 0
                for n in nums:
                    if elem == n:
                        count += 1
                
                if count > len(nums)/k:
                    res.append(elem)
            return res
            
        
        return KmajorityElem(nums, 3)

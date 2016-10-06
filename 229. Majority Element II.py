'''
Problem:

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
The algorithm should run in linear time and in O(1) space.

'''




class Solution(object):
    def majorityElement(self, nums):
        """
            :type nums: List[int]
            :rtype: List[int]
            """
        if not nums or len(nums)<3:
            return list(set(nums))

        res = []
        n1 = None
        n2 = None
        count1 = 0
        count2 = 0

        for n in nums:
            if count1>0 and count2>0:
                if n1 == n:
                    count1 += 1
                if n2 == n:
                    count2 += 1
                else:
                    count1 -= 1
                    count2 -= 1

            elif count1>0:
                if n1 == n:
                    count1 += 1
                else:
                    n2 = n
                    count2 += 1

            elif count2>0:
                if n2 == n:
                    count2 += 1
                else:
                    n1 = n
                    count1 += 1

            else:
                n1 = n
                count1 += 1



        count1 = count2 = 0
        for elem in nums:
            if elem == n1:
                count1 +=1
            elif elem == n2:
                count2 +=1


        if count1 > len(nums)/3:
            res.append(n1)
        if count2 > len(nums)/3:
            res.append(n2)

        return res



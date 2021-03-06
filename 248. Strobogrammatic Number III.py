'''
Problem:

A strobogrammatic number is a number that looks the same when rotated 180 degrees.
Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

For example,
Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobo numbers.

Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''

class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
            :type low: str
            :type high: str
            :rtype: int
            """
        def getStrob(left, n, low, high, count):
            # 2 base cases: n is even and n is odd
            if left == 0: return ['']
            elif left == 1: return ['0','1','8']

            res = getStrob(left-2, n, low, high, count)
            newres = []
            for item in res:
                if left == n:
                    for x in mp.keys():
                        if x == '0': continue
                        elif int(low) <= int(x+item+mp[x]) <= int(high):
                            count[0] += 1  # here update count
                else:
                    for k in mp.keys():
                        newres.append(k+item+mp[k])
            return newres

        

        mp = {'0':'0', '1':'1', '8':'8', '6':'9', '9':'6'}
        count = [0]

        # corner case:
        if int(low)>int(high): return 0

        # corner case for length of 1
        if len(low) == 1:
            for x in ['0','1','8']:
                if int(low) <= int(mp[x]) <= int(high):
                    count[0] += 1
                    
        # recursion for general cases
        for length in range(len(low),len(high)+1):
            getStrob(length,length,low,high,count)
        return count[0]

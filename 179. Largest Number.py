'''
Problem:

    Given a list of non negative integers, arrange them such that they form the largest number.
    For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: 
    The result may be very large, so you need to return a string instead of an integer.
'''

'''
Solution:

    - num.sort(cmp=lambda x,y: cmp(x+y,y+x),reverse=True)
    - trailing zeros: return ''.join(num).lstrip('0') or '0' (if the input is all "0"s, then the result is '0')

    For example, if you compare '3' and '30',
        then the cpm will try to compare '330' and '303', since 330 > 303 => 3 > 30.
        with reverse = True, the result would be [3,30]
'''


class Solution(object):

    def largestNumber(self, nums):
        def __cmp__(x,y):
            return  int(y+x) - int(x+y)

        num = [str(x) for x in nums]
        num.sort(cmp=__cmp__)
        return ''.join(num).lstrip('0') or '0'
        

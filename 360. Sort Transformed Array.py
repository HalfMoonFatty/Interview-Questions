'''
Problem:

    Given a sorted array of integers nums and integer values a, b and c.
    Apply a function of the form f(x) = ax2 + bx + c to each element x in the array.

    The returned array must be in sorted order.

    Expected time complexity: O(n)

Example:

    nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5,

    Result: [3, 9, 15, 33]

    nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5

    Result: [-23, -5, 1, 7]

'''


'''
Solution:

1.a>0, two ends in original array are bigger than center.

2.a<0, center is bigger than two ends.

For a==0 case, it does not matter what b's sign is.The function is monotonically increasing or decreasing. you can start with either beginning or end.

'''


class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
            :type nums: List[int]
            :type a: int
            :type b: int
            :type c: int
            :rtype: List[int]
            """

        def f(x, a, b, c):
            return a*pow(x,2) + b*x + c


        result = [0]*len(nums)
        i,j = 0,len(nums)-1
        index = len(nums)-1 if a >= 0 else 0

        while i <= j:
            if a >= 0:  # from end to begin: 存大的
                if f(nums[i],a,b,c) >= f(nums[j],a,b,c):  # 存大的
                    result[index] = f(nums[i],a,b,c)
                    i += 1
                else:
                    result[index] = f(nums[j],a,b,c)
                    j -= 1
                index -= 1  # from end to begin

            else:   # from begin to end： 存小的
                if f(nums[i],a,b,c) >= f(nums[j],a,b,c):
                    result[index] = f(nums[j],a,b,c)    # 存小的
                    j -= 1
                else:
                    result[index] = f(nums[i],a,b,c)
                    i += 1
                index += 1  # from end to begin

        return result

'''
Problem:
   
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].
   
   
     Example: Given nums = [5, 2, 6, 1]
   
     To the right of 5 there are 2 smaller elements (2 and 1).
     To the right of 2 there is only 1 smaller element (1).
     To the right of 6 there is 1 smaller element (1).
     To the right of 1 there is 0 smaller element.
     Return the array [2, 1, 1, 0].

'''

# segment tree

















# Solution 2 merge sort based
def countSmaller(self, nums):
    def sort(enum):
        mid = len(enum) / 2
        if mid:
            left, right = sort(enum[:mid]), sort(enum[mid:])
            for i in range(len(enum))[::-1]:
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum
        
        
    smaller = [0] * len(nums)
    sort(list(enumerate(nums)))
    return smaller

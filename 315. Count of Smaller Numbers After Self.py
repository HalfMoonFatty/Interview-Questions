'''
Problem:

You are given an integer array nums and you have to return a new counts array. 
The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example: Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
'''

# Solution 1: BIT
# nums = [5, 2, 6, 1]
# sorted:[1, 2, 5, 6]
# index: [1:1, 2:2, 5:3, 6:4]

# The idea is to iterate the array from n-1 to 0. When we are at i'th index, 
# we check how many numbers ranking less than arr[i] are present in BIT and add it to the result. 
# After that we add current element to to the BIT[] by udating count of current element from 0 to 1, 
# and therefore updates ancestors of current element in BIT
# http://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        index = {v:i+1 for i, v in enumerate(sorted(set(nums)))}
        ft = FenwickTree(len(nums))
        ans = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            ans[i] = ft.sum(index[nums[i]]-1)    # not including itself
            ft.add(index[nums[i]], 1)            # add "1" at index iNums[i]
        return ans
    

class FenwickTree(object):
    def __init__(self, n):
        self.n = n
        self.sums = [0] * (n + 1)

    def add(self, index, val):
        while index <= self.n:
            self.sums[index] += val
            index += index & -index

    def sum(self, index):
        res = 0
        while index > 0:
            res += self.sums[index]
            index -= index & -index
        return res
        
        

'''
Solution 2: MergeSort Based

smaller[left[i][0]] += j meaning there are j elements smaller than the current left[i]

For example, nums = [5, 2, 6, 1]

left is: [(0, 5)]; right is [(1, 2)]
i is: 0; j is: 1; smaller array is: [*1, 0, 0, 0]; i.e. j is 1, smaller[indexof(5)] += 1

left is: [(2, 6)]; right is [(3, 1)]
i is: 0; j is: 1; smaller array is: [1, 0, *1, 0]; i.e. j is 1, smaller[indexof(6)] += 1

left is: [(1, 2), (0, 5)]; right is [(3, 1), (2, 6)]
i is: 0; j is: 1; smaller array is: [1, *1, 1, 0]
i is: 1; j is: 1; smaller array is: [*2, 1, 1, 0]
'''

class Solution(object):
    def countSmaller(self, nums):
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                m, n = len(left), len(right)
                i = j = 0
                while i < m or j < n:
                    if j == n or i < m and left[i][1] <= right[j][1]:
                        enum[i+j] = left[i]
                        smaller[left[i][0]] += j
                        i += 1
                    else:
                        enum[i+j] = right[j]
                        j += 1
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller           
            
       
    
# Solution 3: BST

class Solution(object):
    def countSmaller(self, nums):
        ans = [0] * len(nums)
        bst = BinarySearchTree()
        for i in range(len(nums) - 1, -1, -1):
            ans[i] = bst.insert(nums[i])
        return ans

class TreeNode(object):
    def __init__(self, val):
        self.leftCnt = 0
        self.val = val
        self.cnt = 1
        self.left = None
        self.right = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
            return 0
        root = self.root
        cnt = 0
        while root:
            if val < root.val:
                root.leftCnt += 1
                if root.left is None:
                    root.left = TreeNode(val)
                    break
                root = root.left
            elif val > root.val:
                cnt += root.leftCnt + root.cnt
                if root.right is None:
                    root.right = TreeNode(val)
                    break
                root = root.right
            else:
                cnt += root.leftCnt
                root.cnt += 1
                break
        return cnt

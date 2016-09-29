'''
Problem:

    Suppose a sorted array is rotated at some pivot unknown to you beforehand.

    (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

    You are given a target value to search. If found in the array return its index, otherwise return -1.
   
    You may assume no duplicate exists in the array.

'''

        |
        |／│
      ／|  │
    ／  |  │
  ／    |  │  
 │  ②   |① │  ／│ 
 │      |  │／③ │ 
 -------|--------
 s     mid      e



          |
    ／│   |
  ／  │   |
 │    │   |    ／│
 │    │   |  ／  │
 │  ③ │   |／    │
 │    │／①|   ②  │
----------|--------
 s       mid    e






# Solution 1: Binary Search - Iteration Solution

 class Solution(object):
   
    def search(self, nums, target):

        def helper(nums,s,e,tar):
            while s <= e:
            
                mid = s + (e - s)/2
                
                if tar == nums[mid]:
                    return mid
               
                if nums[mid] >= nums[s]:   # >=
                    if tar > nums[mid]:
                        s = mid + 1
                    elif tar >= nums[s]:
                        e = mid - 1
                    else:
                        s = mid + 1
           
                elif tar < nums[mid]:
                    e = mid - 1
               
                elif tar <= nums[e]:    # <=
                    s = mid + 1
               
                else:
                    e = mid - 1
       
                return -1
               
               
            end = len(nums)-1
            start = 0
            return helper(nums,start,end,target)




# Solution 2: Binary Search - Recursive Solution


class Solution(object):
   
    def search(self, nums, target):

        def helper (nums,s,e,tar):
            if s > e:
                return -1
           
            mid = s + (e - s)/2
           
            if tar == nums[mid]:
                return mid
       
            if nums[mid] >= nums[s]:    # >=
                if tar > nums[mid]:
                    s = mid + 1
                elif tar >= nums[s]:    # >=
                    e = mid - 1
                else:
                    s = mid + 1
           
            elif tar < nums[mid]:
                e = mid - 1

            elif tar <= nums[e]:    # <=
                s = mid + 1
           
            else:
                e = mid - 1
       
            return helper (nums,s,e,tar)
       
       
        end = len(nums)-1
        start = 0
        return helper(nums,start,end,target)

'''
Problem

	Given an array of integers, how many three numbers can be found in the array, 
	so that we can build an triangle whose three edges length is the three numbers that we find?

	Example
	Given array S = [3,4,6,7], return 3. They are:
	[3,4,6]
	[3,6,7]
	[4,6,7]
	
	Given array S = [4,4,4,4], return 4. They are:
	[4(1),4(2),4(3)]
	[4(1),4(2),4(4)]
	[4(1),4(3),4(4)]
	[4(2),4(3),4(4)]

'''

def triangleCount(arr):
    arr.sort()
    count = 0
    for i in range(0,n):
        # target = a[i]
        left, right = 0, i-1
        while left < right:
            if a[left] + a[right] > a[i]:
                count += right - left
                right -= 1
            else:
                left += 1
    return count

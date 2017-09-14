def rearrangeStr(nums):
  odd, even = 0, len(nums)-1
  i = 0
  while i <= even and odd <= even:
    if nums[i]%2:
      nums[i], nums[odd] = nums[odd], nums[i]
      odd += 1
      i += 1
    else:
      nums[i], nums[even] = nums[even], nums[i]
      even -= 1

  return nums

#nums = [1,2,3,4,5,6,7,8]
#print rearrangeStr(nums)



def rearange2(nums):
  if len(nums) <= 2:
    return nums
  mid = len(nums)/2
  l1 = rearange2(nums[:mid/2]+nums[mid:mid+mid/2])
  l2 = rearange2(nums[mid/2:mid]+nums[mid+mid/2:])
  return l1+l2



nums = [1,2,3,4,5,6,7,8]
print rearange2(nums)
print rearange2([1,2,3,4])
# [1,3,2,4]
# [1,5,2,6,3,7,4,8]

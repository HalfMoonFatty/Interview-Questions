'''
Problem:
   
Additive number is a string whose digits can form additive sequence.
   
A valid additive sequence should contain at least three numbers. Except for the first two numbers, 
each subsequent number in the sequence must be the sum of the preceding two.
   
   
For example:
"112358" is an additive number because the digits can form an additive sequence: 1, 1, 2, 3, 5, 8.
1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8
   
"199100199" is also an additive number, the additive sequence is: 1, 99, 100, 199.
1 + 99 = 100, 99 + 100 = 199


Note:
    Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.
    Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.
   
   
Follow up:
    How would you handle overflow for very large input integers?

'''

'''
Solution: Time: O(N^2); Space O(N)-recursion

main function - travel through all combinations of length of num1 and num2
Note that the length of first two numbers can't be longer than half of the initial string, so the two loops in the first function will end when i>num.size()/2 and j>(num.size()-i)/2, this will actually save a lot of time.
   
helper function - recursive check substrings 
add the 2 numbers and see if the sum:
- if exactly equals to num3: directly return True
- if the sum is a substring of the remaining string: recursively call on substrings.
   
'''

class Solution(object):
    def isAdditiveNumber(self, num):
       
        def isAddi(num1, num2, num3):
            # check leading zeros of num1 and num2
            if str(int(num1)) != num1 or len(num2)<1 or str(int(num2)) != num2:
                return False
           
            sum12 = str(int(num1) + int(num2))
           
            if sum12 == num3:
                return True
            elif len(num3) < len(sum12) or not num3.startswith(sum12):
                return False
            else:
                return isAddi(num2, sum12, num3[len(sum12):])
       
       
        # travel through all combinations of length of num1 and num2
        for i in range(1,len(num)/2+1):         # i is the length of number 1 start from 1
            for j in range(1,(len(num)-i)/2+1): # j is the length of number 2 start from 1
                if isAddi(num[0:i],num[i:i+j],num[i+j:]):
                    return True
        return False


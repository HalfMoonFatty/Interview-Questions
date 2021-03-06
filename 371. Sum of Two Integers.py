'''
Problem:

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''


int Add(int x, int y)
{
    // Iterate till there is no carry  
    while (y != 0)
    {
        // carry now contains common set bits of x and y
        int carry = x & y;  
 
        // Sum of bits of x and y where at least one of the bits is not set
        x = x ^ y; 
 
        // Carry is shifted by one so that adding it to x gives the required sum
        y = carry << 1;
    }
    return x;
}



class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign. 
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer. 
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a

'''
Idea:
Adding two integers a and b (no matter positive or negative) can always be boiled down into 3 steps:

1. convert a and b into two's complements.
2. add both two's complements. The result is a new two's complement
3. convert the result back to integer

Two things to note:

In Python, every integer is associated with its two's complement and its sign. 
However, doing bit operation "& mask" loses the track of sign. For example, -1 & 0xffffffff becomes a huge positive number 4294967295. 
Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
The magic is that if there is a negative integer n, and its unsigned 32-bit two's complement is m, 
then m = ~(n ^ 0xffffffff) and n = ~(m ^ 0xffffffff). So using this magic, you can do the conversion in step 3.
'''

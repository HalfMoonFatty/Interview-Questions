'''
Problem:

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,
123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Hint:
Did you see a pattern in dividing the number into chunk of words? For example, 123 and 123000.
Group the number by thousands (3 digits). You can write a helper function that takes a number less than 1000 and convert just that chunk to words.

There are many edge cases. What are some good test cases? Does your code work with input such as 0? Or 1000010? (middle chunk is zero and should not be printed out)
'''

'''
Solution: Time: O(N); Space O(1)

    - Main Function (numberToWords): iteration 三个一组分组在这里
        Iterate through the number and group the number by thousands (3 digits) from left(LSB) to right(MSB).
       
    - Helper Function (helper): recursion 分情况讨论在这里
        - num<20
        - num<100
        - num>100
        注意空格
          
'''


class Solution(object):
    def numberToWords(self, num):
       
        # Recursion
        def helper(num):
            if num == 0:
                return ""
            elif num < 20:
                return lessThan20[num] + " "
            elif num < 100:
                return tens[num/10] + " " + helper(num%10)
            else:
                return lessThan20[num/100] + " Hundred " + helper(num%100)
       
       
       
        lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]
       
        # Special case
        if num == 0: return "Zero"
   
        # Iteration
        engWords = ""
        i = 0
        while num > 0:
            if num%1000 != 0:
                engWords = helper(num%1000) + thousands[i] + " " + engWords # left LSB to MSB
            i += 1
            num /= 1000
        return engWords.lstrip().rstrip() # get rid of space in the beginning and at the end



'''
Problem:

The API: int read4(char *buf) reads 4 characters at a time from a file.
The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
     The read function will only be called once for each test case.

Similar Problems:
     (E) 157. Read N Characters Given Read4
     (H) 158. Read N Characters Given Read4 II - Call multiple times
'''

'''
Solution:

'''

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
        buff = [None]*4
        EOF = False
        total = 0

        while total < n and not EOF:
            count = read4(buff)     # call read4(buf): to read into internal buffer
            if count < 4:
                EOF = True
            length = min(n-total, count)
            for i in range(length):
                buf[total+i] = buff[i]
            total += length
        return total

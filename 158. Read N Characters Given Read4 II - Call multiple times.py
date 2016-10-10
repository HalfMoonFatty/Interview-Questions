'''
Problem:

    The API: int read4(char *buf) reads 4 characters at a time from a file.
    The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
    By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

Note:
    The read function may be called multiple times.
    
'''

'''
Solution:

    - Use "offset" and "buffPtr" to store the data received in previous calls.
    - In the while loop, if offset reaches current buffPtr, it will be set as zero to be ready to read new data.
    - The globalPtr is the pointer for the buf(destination), so it gets reset for every function call.

    There are 2 cases need to pay extra attention:
    case 1: After calling read4 to read chars. If there is nothing read in, get out of the loop (if self.buffPtr == 0: break).
    case 2: when copying data from internal tmp buffer(buff), we not only need to be careful not go beyond the tmp buffer but also need to prevent globalPtr go beyond n (intended). 
    For example, if n = 6, the first iteration we read in 4 chars (by calling read4(buff)), and globalPtr will be 4 after drain the internal buffer; 
    the second iteration, we read in 4 chars again, but this time we only need 2 more chars, so we have be prevent globalPtr increase to 8 (greater than 6).

'''


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buff = [None]*4
        self.buffPtr = 0
        self.offset = 0


    def read(self, buf, n):
        """
            :type buf: Destination buffer (List[str])
            :type n: Maximum number of characters to read (int)
            :rtype: The number of characters read (int)
            """
        globalPtr = 0
        while globalPtr < n:
         
            # no more data in the internal buffer, need to read in new data
            if self.offset == 0:
                self.buffPtr = read4(self.buff)

            # have nothing to read-in
            if self.buffPtr == 0:
                break

            # 搬砖ing, 一次搬4块
            while globalPtr < n and self.offset < self.buffPtr:    # note loop condition
                buf[globalPtr] = self.buff[self.offset]
                self.offset += 1
                globalPtr += 1

            # drained up the internal buffer, reset the offset to 0
            if self.offset >= self.buffPtr:
                self.offset = 0

        return globalPtr

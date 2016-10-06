'''
Problem:

    Design a Phone Directory which supports the following operations:

    1. get: Provide a number which is not assigned to anyone.
    2. check: Check if a number is available or not.
    3. release: Recycle or release a number.

Example:

    // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
    PhoneDirectory directory = new PhoneDirectory(3);

    // It can return any available phone number. Here we assume it returns 0.
    directory.get();

    // Assume it returns 1.
    directory.get();

    // The number 2 is available, so return true.
    directory.check(2);

    // It returns 2, the only number that is left.
    directory.get();

    // The number 2 is no longer available, so return false.
    directory.check(2);

    // Release number 2 back to the pool.
    directory.release(2);

    // Number 2 is available again, return true.
    directory.check(2);

'''

'''
Solution 1:

'''

from sets import Set
class PhoneDirectory(object):

    def __init__(self, maxNumbers):

        self.maxNumbers = maxNumbers
        self.used = Set()
        self.pool = [i for i in range(maxNumbers)]


    def get(self):

        if self.pool:
            n = self.pool.pop()
            self.used.add(n)   # note
            return n
        else:
            return -1



    def check(self, number):

        if number < 0 or number > self.maxNumbers:    # note
            return False
        return number not in self.used



    def release(self, number):

        if number in self.used:    # note
          self.used.remove(number)
          self.pool.append(number)
        

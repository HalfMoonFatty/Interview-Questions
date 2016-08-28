'''
Problem:

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

Similar Problems:
(E) 346. Moving Average from Data Stream
(H) 295. Find Median from Data Stream

'''

'''
Solution 1: Take advantage of using deque with maxlen parameter.
'''

from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        self.queue = collections.deque(maxlen=size)

    def next(self, val):
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)


'''
The following code is a bit more verbose.
'''

from collections import deque
class MovingAverage(object):

    def __init__(self, size):
        self.window_size = size
        self.queue = deque()
        self.sum = 0

    def next(self, val):

        # if queue is already full, pop the left element
        if len(self.queue) == self.window_size:
            self.sum -= self.queue.popleft()

        # same logic for both cases where queue is full or not
        self.queue.append(val)
        self.sum += val
        return self.sum/len(self.queue)

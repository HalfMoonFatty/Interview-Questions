'''
Problem:

Design a simplified version of Twitter where users can post tweets, follow/unfollow another user and is able to see the 10 most recent tweets in the user's news feed. Your design should support the following methods:

- postTweet(userId, tweetId): Compose a new tweet.
- getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
- follow(followerId, followeeId): Follower follows a followee.
- unfollow(followerId, followeeId): Follower unfollows a followee.

Example:

Twitter twitter = new Twitter();

// User 1 posts a new tweet (id = 5).
twitter.postTweet(1, 5);

// User 1's news feed should return a list with 1 tweet id -> [5].
twitter.getNewsFeed(1);

// User 1 follows user 2.
twitter.follow(1, 2);

// User 2 posts a new tweet (id = 6).
twitter.postTweet(2, 6);

// User 1's news feed should return a list with 2 tweet ids -> [6, 5].
// Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.getNewsFeed(1);

// User 1 unfollows user 2.
twitter.unfollow(1, 2);

// User 1's news feed should return a list with 1 tweet id -> [5],
// since user 1 is no longer following user 2.
twitter.getNewsFeed(1);

'''

'''
Solution 1: OO Design

User:
    Attributes:
    + userId
    + tweets postes by the user
    + followee list

    Functions:
    - follow(followeeId) # Using set()
    - unfollow(followeeId) # Using set()
    - post(tweet)


Tweet:
    Attributes:
    + tweetId
    + time when the tweet is posted

Twitter:
    Attributes:
    + Timestamp (global Timestamp assgin to each tweet)
    + userMap <userId, User> # Using hashtable

    Function:
    - createUser(userId)
    - postTweet(userId, tweetId)
    - getNewsFeed(userId) # Using heapq
    - follow(followerId, followeeId)
    - unfollow(followerId, followeeId)

'''

class Twitter(object):
    class User(object):

        def __init__(self, userId):
            self.userid = userId
            self.tweets = []
            self.followee = set([userId])  #init the user to follow himself

        def follow(self,followeeId):
            self.followee.add(followeeId)

        def unfollow(self,followeeId):
            self.followee.discard(followeeId)

        def post(self, tweetId, Timestamp):
            tweet = Twitter.Tweet(tweetId,Timestamp)
            self.tweets.append(tweet)


            
    class Tweet(object):

        def __init__(self, tweetId, Timestamp):
            self.tweetId = tweetId
            self.time = Timestamp

            

    def __init__(self):
        self.Timestamp = 0
        self.userMap = {}


    def createUser(self, userId):
        newUser = self.User(userId)
        self.userMap[userId] = newUser


    def postTweet(self, userId, tweetId):
        if not self.userMap.has_key(userId):
            self.createUser(userId)
        self.userMap[userId].post(tweetId, self.Timestamp)
        self.Timestamp += 1


    # using min heap size = 10 to get 10 most recent (max) time tweet
    def getNewsFeed(self, userId):
        """
            Retrieve the 10 most recent tweet ids in the user's news feed. 
            Each item in the news feed must be posted by users who the user followed or by the user herself. 
            Tweets must be ordered from most recent to least recent.
            :type userId: int
            :rtype: List[int]
            """
        heap = []
        if not self.userMap.has_key(userId):
            return heap
            
        followeeIds = self.userMap[userId].followee
        for fId in followeeIds:
            for t in self.userMap[fId].tweets:
                if len(heap) < 10:
                    heapq.heappush(heap, [t.time, t.tweetId] )
                else:
                    if t.time > heap[0][0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, [t.time, t.tweetId] )
        
        news = []         
        while len(heap)>0:
            news.append(heapq.heappop(heap)[1])
        return news[::-1]



    def follow(self, followerId, followeeId):
        """
            Follower follows a followee. If the operation is invalid, it should be a no-op.
            """
        if not self.userMap.has_key(followerId):
            self.createUser(followerId)
        if not self.userMap.has_key(followeeId):
            self.createUser(followeeId)
        follower = self.userMap[followerId]
        follower.follow(followeeId)



    def unfollow(self, followerId, followeeId):
        """
            Follower unfollows a followee. If the operation is invalid, it should be a no-op.
            """
        if not self.userMap.has_key(followerId) or followerId == followeeId: # user cannot unfollow himself
            return
        self.userMap[followerId].unfollow(followeeId)


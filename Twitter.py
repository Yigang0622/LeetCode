# LeetCode
# Twitter 
# Created by Yigang Zhou on 2020/11/8.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 355. 设计推特
# https://leetcode-cn.com/problems/design-twitter/
from typing import List
import collections

class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # user_id:[follower_id]
        self.follower_dict = dict()
        self.tweets = collections.deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        tweet = (tweetId, userId)
        self.tweets.appendleft(tweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        tweets_fetched = []
        count = 0
        for tweetId, u_id in self.tweets:
            if u_id == userId:
                tweets_fetched.append(tweetId)
                count += 1
            elif userId in self.follower_dict and u_id in self.follower_dict[userId]:
                tweets_fetched.append(tweetId)
                count += 1
            if count == 10:
                return tweets_fetched
        return tweets_fetched

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower_dict:
            self.follower_dict[followerId].add(followeeId)
        else:
            self.follower_dict[followerId] = {followeeId}


    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follower_dict and followeeId in self.follower_dict[followerId]:
            self.follower_dict[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
print(param_2)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
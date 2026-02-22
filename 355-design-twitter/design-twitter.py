class Twitter:

    def __init__(self):
        self.time=0
        self.followers=defaultdict(set)
        self.tweets=defaultdict(list)
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap=[]
        self.followers[userId].add(userId)
        for f in self.followers[userId]:
            if self.tweets[f]:
                ind=len(self.tweets[f])-1
                time,tweetId=self.tweets[f][ind]
                heapq.heappush(heap,(-time,tweetId,f,ind))
        res=[]
        for i in range(10):
            if not heap:
                break
            time,tweetId,f,ind=heapq.heappop(heap)
            res.append(tweetId)
            if ind-1>=0:
                ntime,ntweetId=self.tweets[f][ind-1]
                heapq.heappush(heap,(-ntime,ntweetId,f,ind-1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
class VideoSharingPlatform:

    def __init__(self):
        self.id = 0
        self.cach = set()
        self.heap = []
        self.content = defaultdict(lambda:"")
        self.views = defaultdict(lambda:-1)
        self.likes = defaultdict(lambda:-1)
        self.dislikes = defaultdict(lambda:-1)


    def upload(self, video: str) -> int:
        while self.heap and self.heap[0] not in self.cach:
            heappop(self.heap)
        if self.heap:
            x = heappop(self.heap)
            self.cach.remove(x)
        else:
            x = self.id
            self.id += 1
        self.content[x] = video
        self.views[x] = 0
        self.likes[x] = 0
        self.dislikes[x] = 0
        return x


    def remove(self, videoId: int) -> None:
        if videoId >= self.id or videoId in self.cach:
            return
        self.cach.add(videoId)
        heappush(self.heap, videoId)
        self.content[videoId] = ""
        self.views[videoId] = -1
        self.likes[videoId] = -1
        self.dislikes[videoId] = -1


    def watch(self, videoId: int, startMinute: int, endMinute: int) -> str:
        if not self.content[videoId]:
            return "-1"
        leng = len(self.content[videoId])
        self.views[videoId] += 1
        return self.content[videoId][startMinute:min(endMinute+1,leng)]


    def like(self, videoId: int) -> None:
        if self.likes[videoId] == -1:
            return
        self.likes[videoId] += 1


    def dislike(self, videoId: int) -> None:
        if self.dislikes[videoId] == -1:
            return
        self.dislikes[videoId] += 1


    def getLikesAndDislikes(self, videoId: int) -> List[int]:
        if self.likes[videoId] == -1:
            return [-1]
        return [self.likes[videoId], self.dislikes[videoId]]


    def getViews(self, videoId: int) -> int:
        return self.views[videoId]



# Your VideoSharingPlatform object will be instantiated and called as such:
# obj = VideoSharingPlatform()
# param_1 = obj.upload(video)
# obj.remove(videoId)
# param_3 = obj.watch(videoId,startMinute,endMinute)
# obj.like(videoId)
# obj.dislike(videoId)
# param_6 = obj.getLikesAndDislikes(videoId)
# param_7 = obj.getViews(videoId)
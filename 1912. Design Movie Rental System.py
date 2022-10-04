class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.films = defaultdict(list)
        self.delay1 = defaultdict(set)
        self.rented = []
        self.delay2 = set()
        self.saved = defaultdict(lambda:Counter())
        for shop, movie, price in entries:
            self.saved[shop][movie] = price
            heappush(self.films[movie], (price, shop))


    def search(self, movie: int) -> List[int]:
        res = []
        added = []
        while self.films[movie] and len(res) < 5:
            while self.films[movie] and self.films[movie][0][1] in self.delay1[movie]:
                self.delay1[movie].remove(self.films[movie][0][1])
                heappop(self.films[movie])
            if self.films[movie]:
                res.append(self.films[movie][0][1])
                added.append(heappop(self.films[movie]))
        while added:
            heappush(self.films[movie], added.pop())
        return res


    def rent(self, shop: int, movie: int) -> None:
        self.delay1[movie].add(shop)
        if (shop, movie) in self.delay2:
            self.delay2.remove((shop, movie))
        else:
            heappush(self.rented, (self.saved[shop][movie], shop, movie))


    def drop(self, shop: int, movie: int) -> None:
        self.delay2.add((shop, movie))
        if shop in self.delay1[movie]:
            self.delay1[movie].remove(shop)
        else:
            heappush(self.films[movie], (self.saved[shop][movie], shop))


    def report(self) -> List[List[int]]:
        res = []
        added = []
        while self.rented and len(res) < 5:
            while self.rented and (self.rented[0][1], self.rented[0][2]) in self.delay2:
                self.delay2.remove((self.rented[0][1], self.rented[0][2]))
                heappop(self.rented)
            if self.rented:
                res.append([self.rented[0][1], self.rented[0][2]])
                added.append(heappop(self.rented))
        while added:
            heappush(self.rented, added.pop())
        return res



# Your MovieRentingSystem object will be instantiated and called as such:
# obj = MovieRentingSystem(n, entries)
# param_1 = obj.search(movie)
# obj.rent(shop,movie)
# obj.drop(shop,movie)
# param_4 = obj.report()
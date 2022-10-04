class Solution:
    def minBuildTime(self, blocks: List[int], split: int) -> int:
        heapify(blocks)
        while len(blocks) > 1:
            x = heappop(blocks)
            y = heappop(blocks)
            heappush(blocks, max(x,y) + split)
        return blocks[0]

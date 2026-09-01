class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for cur in range(len(flowerbed)):
            if flowerbed[cur] == 0:
                prev_pt = (cur == 0) or (flowerbed[cur - 1] == 0) 
                next_pt = (cur == len(flowerbed) - 1) or (flowerbed[cur + 1] == 0)

                if prev_pt and next_pt:
                    flowerbed[cur] = 1
                    n -= 1
                    if n <= 0:
                        return True
        return n <= 0
        
        
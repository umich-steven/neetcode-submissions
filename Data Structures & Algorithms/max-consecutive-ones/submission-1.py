class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        best = 0

        for i, value in enumerate(nums):
            
            current = current + 1 if value else 0
            best = max(best, current)
        return best
        
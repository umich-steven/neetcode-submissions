class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Keep track of every value I've seen so far
        # Loop through nums: Iteration of lists is O(n)
        # If current num was already seen, return True: set O(1)
        # Otherwise add it to seen: 
        # If the loop finishes, return False
        # Use a data structure
        tracker = set()

        for num in nums:
            if num in tracker:
                return True
            else:
                tracker.add(num)

        return False
        

        
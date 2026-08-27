class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        total = 2 * len(nums)
        arr = [0] * total
        for i in range(len(nums)):
            arr[i] = nums[i]
            arr[len(nums) + i] = nums[i]
            

        return(arr)
        
       
            

      
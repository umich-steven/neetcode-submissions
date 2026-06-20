class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        int_table = {}
        for i, num in enumerate(nums):
            print(i, num)
            remainder = target - num
            if remainder in int_table:
                return[int_table[remainder], i]
            int_table[num] = i

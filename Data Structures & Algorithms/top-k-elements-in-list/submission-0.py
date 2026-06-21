class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table[i] += 1
            else:
                hash_table[i] = 1
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in hash_table.items():
            buckets[count].append(num)

        print(buckets)
        result = []
        for i in range(len(nums), 0, -1):
            print(i)
            for num in buckets[i]:
                print(num)
                result.append(num)
                if len(result) == k:
                    return result        
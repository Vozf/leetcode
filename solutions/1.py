class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, el in enumerate(nums):
            key = target - el
            if el in dic:
                return [dic[el], i]
            dic[key] = i

        

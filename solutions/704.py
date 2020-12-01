
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)
        while i < j:
            k = (i + j) >> 1
            if nums[k] == target:
                    break
            elif nums[k] < target:
                    i = k + 1
            else:
                    j = k
        if nums[k] == target:
            return k
        else: 
            return -1
	

        

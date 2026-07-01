class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmaps = {}
        for i,n in enumerate(nums):
            diff = target-n
            if diff in prevmaps:
                return [prevmaps[diff], i]
            prevmaps[n] = i
        return


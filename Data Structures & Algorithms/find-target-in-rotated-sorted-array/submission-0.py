class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for t in range(len(nums)):
            if nums[t] == target:
                return t
        return -1
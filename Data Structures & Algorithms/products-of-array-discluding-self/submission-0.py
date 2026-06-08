class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for n in range(len(nums)):
            mul = 1
            for i in range(len(nums)):
                if n == i:
                    continue
                mul = mul * nums[i]
            res.append(mul)
        return res
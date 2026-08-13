class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n == 0:
            return 0
        count = 1
        l=1
        for i in range(n-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] - nums[i] == 1:
                count = count + 1
            else:
                count = 1
            l = max(count,l)
        return l
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        c=1
        ans=1

        if n==0:
            return 0

        for i in range(n-1):
            if nums[i+1]==nums[i]:
                continue
            elif nums[i+1]==nums[i]+1:
                c+=1
            else:
                c=1
            ans=max(ans,c)
        return ans



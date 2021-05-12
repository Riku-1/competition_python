class Solution:
    def findMaxConsecutiveOnes(self, nums: [int]) -> int:
        con_list = [0 for i in nums]
        for i, v in enumerate(nums):
            if v == 1:
                if i == 0:
                    con_list[i] = 1
                else:
                    con_list[i] = con_list[i-1] + 1

        return max(con_list)

c = Solution()
print(c.findMaxConsecutiveOnes([1, 1, 1]))


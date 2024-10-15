# 2938. Separate Black and White Balls
# https://leetcode.com/problems/separate-black-and-white-balls/
class Solution:
    def minimumSteps(self, s: str) -> int:
        ans = 0
        zi = 0
        i = 0
        for char in s:
            if char == '0':
                ans += (i - zi)
                zi += 1
            i += 1
        return ans


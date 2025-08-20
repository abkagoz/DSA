class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        hill = 0
        out = 0
        old = 0

        while l <= r:
            hill = min(height[l], height[r])
            if old < hill:
                for i in range(l, r):
                    if height[i] < hill:
                        out += hill - height[i]
                        height[i] = hill
            old = hill
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return out
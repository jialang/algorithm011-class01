class Solution:
    def trap(self, height):
        left, right = 0, len(height)-1
        maxL, maxR = 0, 0
        res = 0
        while left <= right:
            if height[left] <= height[right]:
                if height[left] >= maxL: 
                    maxL = height[left]
                else:
                    res += maxL - height[left]
                left += 1
            else:
                if height[right] >= maxR:
                    maxR = height[right]
                else:
                    res += maxR - height[right]
                right -= 1
        return res

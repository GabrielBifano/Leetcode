# Container With Most Water
# Medium

def maxArea(height: 'list[int]') -> int:
    
    i = maxArea = 0
    j = len(height) - 1

    while i < j:
        
        h0, h1 = height[i], height[j]
        area = (j - i) * min(h0, h1)

        if area > maxArea:
            maxArea = area
        
        i += h0 <=  h1
        j -= h0  >  h1

    return maxArea
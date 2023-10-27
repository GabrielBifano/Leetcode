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
        
        if h0 < h1:
            i += 1
        elif h1 < h0:
            j -= 1
        else:
            j -= (height[i+1]  >  height[j-1]) # 1 or 0
            i += (height[i+1] <=  height[j-1]) # 1 or 0

    return maxArea
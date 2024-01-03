# Min Cost Climbing Stairs
# Medium

class Solution:
    def minCostClimbingStairs(self, cost: 'list[int]') -> int:
        
        total = [0] * len(cost)
        total[0], total[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            total[i] = min(total[i-1], total[i-2]) + cost[i]
        
        return min(total[-1], total[-2])
            
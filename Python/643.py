# Maximum Average Subarray I
# Easy

def findMaxAverage(nums: 'list[int]', k: int) -> float:
    maxsum = sum(nums[:k]) / k
    window = maxsum
    for i in range(1, len(nums) - k + 1):
        j = i + k - 1
        window = window - nums[i - 1]/k + nums[j]/k
        if window > maxsum:
            maxsum = window
    return maxsum
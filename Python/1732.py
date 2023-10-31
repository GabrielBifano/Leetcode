# Find the Highest Altitude
# Easy

def largestAltitude(gain: 'list[int]') -> int:
    max = alt = 0
    for change in gain:
        alt += change
        if alt > max:
            max = alt
    return max
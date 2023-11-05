# Number of Recent Calls
# Easy

from collections import deque

class RecentCounter:

    def __init__(self):
        self.reqs = deque()
        self.size = 0

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        self.size += 1
        while self.reqs[0] < t - 3000:
            self.size -= 1
            self.reqs.popleft()
        return len(self.reqs)
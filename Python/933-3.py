# Number of Recent Calls
# Easy

from collections import deque

class RecentCounter:

    def __init__(self):
        self.reqs = deque()

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        while self.reqs[0] < t - 3000:
            self.reqs.popleft()
        return len(self.reqs)
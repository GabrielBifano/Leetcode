# Number of Recent Calls
# Easy

class RecentCounter:

    def __init__(self):
        self.reqs = []
        self.size = 0

    def ping(self, t: int) -> int:
        self.reqs.append(t)
        self.size += 1
        
        count = 0
        for mil in reversed(self.reqs):
            if mil < t - 3000:
                break
            count += 1
        return count
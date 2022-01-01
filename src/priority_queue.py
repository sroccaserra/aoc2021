from heapq import heappush, heappop


# Taken from:
# - https://stanford-cs221.github.io/autumn2019/live/search1/
class PriorityQueue:
    def  __init__(self, values=[]):
        self.DONE = -100000
        self.heap = []
        self.priorities = {}  # Map from state to priority
        for state, priority in values:
            self.update(state, priority)

    def update(self, state, newPriority):
        oldPriority = self.priorities.get(state)
        if oldPriority == None or newPriority < oldPriority:
            self.priorities[state] = newPriority
            heappush(self.heap, (newPriority, state))
            return True
        return False

    def removeMin(self):
        while len(self.heap) > 0:
            priority, state = heappop(self.heap)
            if self.priorities[state] == self.DONE:
                continue  # Outdated priority, skip
            self.priorities[state] = self.DONE
            return (state, priority)
        return (None, None) # Nothing left...

from collections import defaultdict


class LfuCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.n = capacity
        self.table = {}
        self.counts = {}
        self.buckets = defaultdict(list)
        self.min = -1

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.table:
            return -1

        count = self.counts[key]
        self.counts[key] = count + 1
        self.buckets[count].remove(key)

        if count == self.min and len(self.buckets[count]) == 0:
            self.min += 1

        self.buckets[count + 1].append(key)

        return self.table[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.n <= 0:
            return

        if key in self.table:
            self.table[key] = value
            self.get(key)
            return

        if len(self.table) >= self.n:
            to_evict = self.buckets[self.min].pop(0)
            del self.table[to_evict]

        self.table[key] = value
        self.counts[key] = 1
        self.min = 1
        self.buckets[1].append(key)

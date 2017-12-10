class CircularArray:
    __slots__ = '_list', '_front', '_rear', '_n'

    def __init__(self, n):
        self._list = [None for _ in range(n)]
        self._n = n
        self._front = 0
        self._rear = 0

    def size(self):
        if self._rear >= self._front:
            return self._rear - self._front
        return self._n - (self._front - self._rear)

    def enqueue(self, item):
        size = self.size()
        if size == self._n - 1:
            self._resize(lambda x: x * 2)
        self._list[self._rear] = item
        self._rear = (self._rear + 1) % self._n

    def dequeue(self):
        size = self.size()
        if size == 0:
            raise RuntimeError("Empty")
        data = self._list[self._front]
        self._list[self._front] = float("inf")
        self._front = (self._front + 1) % self._n
        return data

    def _resize(self, strategy_f):
        new_size = strategy_f(self._n)
        xs = [None for _ in range(new_size)]
        i = self._front
        j = 0
        while i != self._rear:
            xs[j] = self._list[i]
            i = (i + 1) % self._n
            j += 1

        self._front = 0
        self._rear = j
        self._n = new_size
        self._list = xs


if __name__ == '__main__':
    arr = CircularArray(5)
    arr.enqueue(1)
    arr.enqueue(2)
    arr.enqueue(3)
    print(arr.dequeue())
    print(arr.dequeue())
    arr.enqueue(9)
    arr.enqueue(4)
    arr.enqueue(5)
    arr.enqueue(6)
    arr.enqueue(7)
    arr.enqueue(8)
    arr

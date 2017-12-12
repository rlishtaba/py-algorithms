from py_algorithms.caches import new_lru_cache


class TestLruCache:
    def test_put(self):
        cache = new_lru_cache(3)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.put(3, 3)
        cache.put(4, 4)
        assert cache.get(2) == 2
        assert cache.head.key == 2
        assert cache.tail.key == 3
        cache.put(5, 5)
        assert cache.head.key == 5
        assert cache.tail.key == 4
        assert cache.get(2) is 2
        assert cache.get(4)
        assert cache.head.key == 4
        assert cache.tail.key == 5
        cache.put(6, 6)
        assert cache.get(3) is -1
        assert cache.head.key == 6
        assert cache.tail.key == 2
        assert cache.get(3) is -1

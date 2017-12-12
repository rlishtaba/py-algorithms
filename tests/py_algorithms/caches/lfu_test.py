from py_algorithms.caches import new_lfu_cache


class TestLruCache:
    def test_put(self):
        cache = new_lfu_cache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        assert cache.get(1) == 1
        cache.put(3, 3)
        assert cache.get(2) == -1
        assert cache.get(3) == 3
        cache.put(4, 4)
        assert cache.get(1) == -1
        assert cache.get(3) == 3
        assert cache.get(4) == 4

    def test_put_2(self):
        cache = new_lfu_cache(2)
        cache.put(2, 1)
        cache.put(3, 2)
        assert cache.get(3) == 2
        assert cache.get(2) == 1
        cache.put(4, 3)
        assert cache.get(2) == 1
        assert cache.get(3) == -1
        assert cache.get(4) == 3

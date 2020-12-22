
# solve as is, which makes sum a O(k) operations
# maybe improve with trie storing keys

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._map = {}
        

    def insert(self, key: str, val: int) -> None:
        self._map[key] = val
        

    def sum(self, prefix: str) -> int:
        return sum([v for k, v in self._map.items() if k.startswith(prefix)])
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
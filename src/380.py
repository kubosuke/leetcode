from typing import Set


class RandomizedSet:
    def __init__(self):
        self.s = set()

    def insert(self, val: int) -> bool:
        self.s.add(val)
        return True

    def remove(self, val: int) -> bool:
        try:
            self.s.remove(val)
            return True
        except KeyError:
            return False

    def getRandom(self) -> int:
        self.s.pop()


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
obj.insert(1)
obj.remove(2)
obj.insert(2)
obj.getRandom()
obj.remove(1)
obj.insert(2)
obj.getRandom()

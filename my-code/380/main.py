from random import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.mapping = dict()

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False
        self.nums.append(val)
        self.mapping[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mapping:
            return False
        idx = self.mapping[val]
        self.nums[idx] = self.nums[-1]
        self.mapping[self.nums[idx]] = idx
        self.nums.pop()
        del self.mapping[val]
        return True

    def getRandom(self) -> int:
        return self.nums[int(random() * len(self.nums))]


if __name__ == "__main__":
    obj = RandomizedSet()
    print(obj.insert(0))
    print(obj.insert(1))
    print(obj.remove(0))
    print(obj.insert(2))
    print(obj.remove(1))
    print(obj.getRandom())
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class HashTable:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.hashtable = {}



    def insert(self, key: int, value: int) -> None:
        if key not in self.hashtable:
            self.size += 1
        self.hashtable[key] = value
        if (self.size/self.capacity) >= 0.5:
            self.resize()


    def get(self, key: int) -> int:
        if key in self.hashtable:
            return self.hashtable[key]
        return -1


    def remove(self, key: int) -> bool:
        if key not in self.hashtable:
            return False
        del self.hashtable[key]
        self.size -= 1
        return True


    def getSize(self) -> int:
        return self.size


    def getCapacity(self) -> int:
        return self.capacity


    def resize(self) -> None:
        self.capacity = self.capacity * 2


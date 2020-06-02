class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.location = 0
    def append(self, item):
        if ( len(self.storage) == self.capacity ):
            self.storage[self.location] = item
            self.location += 1
            if ( self.location >= self.capacity ):
                self.location = 0
        else:
            self.storage.append(item)
    def get(self):
        return self.storage

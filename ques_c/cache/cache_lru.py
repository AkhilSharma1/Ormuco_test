class LRUCache:
    def __init__(self):
        # self.expiry = expiry
        self.storage = {}

    def size(self,):
        return len(self.storage)

    def get(self, key):
        return self.storage.get(key, None)

    def put(self, key, val):
        self.storage[key] = val

    def update(self, key, val):
        self.storage[key] = val

    def delete(self, key):
        del self.storage[key]

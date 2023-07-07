class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        if self.size() == 0 :
            return True
        else : False
        

    def push(self, item):
        if self.full():
            pass
        else :
            self.items.append(item)
        
    def pop(self):
        if self.isEmpty() :
            return None
        else :
            return self.items.pop()

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() == self.limit :
            return True
        else :
            return False

    def search(self, target):
        for ele in self.items :
            if ele == target :
                return self.size() - self.items.index(target) - 1
        return -1

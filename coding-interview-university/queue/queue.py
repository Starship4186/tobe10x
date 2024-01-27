class Queue:
    '''
    First-In First-Out
    Push value at the end, pop from the start
    '''
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
        

    def dequeue(self):
        if len(self.queue) > 0:
            key = self.queue[0]
            self.queue = self.queue[1::]
            return key
        else:
            return ""

    def display(self):
        return(" ".join((str(i) for i in self.queue)))

    def is_empty(self):
        return True if len(self.queue) == 0 else False


q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("content of the queue: " + q.display())

print(q.is_empty())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print("content of the queue: " + q.display())